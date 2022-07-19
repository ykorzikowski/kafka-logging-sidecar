import time
import os
import json
import json_util
from kafka import KafkaProducer
from subprocess import Popen, PIPE
import shlex

LOGFILE = os.getenv('LOGFILE', default=None)

try:
    KAFKA_SERVER: list = ast.literal_eval(os.getenv('KAFKA_SERVER', default=None))
except:
    log.error('this is not a valid list %s. Try KAFKA_SERVER="[kafka-a, kafka-b]"', os.getenv('KAFKA_SERVER'))
    exit(1)

KAFKA_TOPIC = os.getenv('KAFKA_TOPIC', default=None)

if KAFKA_TOPIC == None or KAFKA_SERVER == None:
    NO_KAFKA = 1
    KAFKA_PRODUCER = None
else:
    NO_KAFKA = 0
    KAFKA_PRODUCER = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

def pretty_print_json(line: str):
    try:
        pretty_json = json.loads(line)
        print(json.dumps(pretty_json, indent=4, sort_keys=True))
    except:
        print ('Not a valid json ' + line)

def write_to_kafka(sline: str):
    KAFKA_PRODUCER.send(KAFKA_TOPIC, json.dumps(line, default=json_util.default).encode('utf-8'))
    KAFKA_PRODUCER.flush()

def process_line(line: str):
    if NO_KAFKA == 1:
        pretty_print_json(line)
    else:
        write_to_kafka(line)

def read_from_logfile():
    logfile = open(LOGFILE,"r")
    loglines = follow(logfile)
    for line in loglines:
        process_line(line)

def read_from_process_stdout():
    cmd = "./fetchLogs.sh"
    process = Popen(shlex.split(cmd), stdout=PIPE)
    with process.stdout:
        for line in iter(process.stdout.readline, b''):
            process_line(line)

if __name__ == '__main__':
    if LOGFILE == None:
        read_from_process_stdout()
    else:
        read_from_logfile()