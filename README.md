# Kafka logging sidecar
a docker image, using python, which reads json-logs from file or directly from stdout and output this to a kafka topic. When no kafka parameters supplied, it wil prettify the json and print to STDOUT. 


## Read from STDOUT, prettify only
Define your `PROCESS_GREP_REGEX`. For example, you can use `[j]ava` to grep for a java process. 

```
- image: ykorzikowski/kafka-logging-sidecar
  name: kafka-logging-sidecar
  resources: {}
  env:
    - name: PROCESS_GREP_REGEX
      value: "[j]ava"
  volumeMounts:
    - mountPath: /home/one/logs
      name: log-path
```

## Read from STDOUT, write to kafka
Define your `PROCESS_GREP_REGEX`. For example, you can use `[j]ava` to grep for a java process. 

```
- image: ykorzikowski/kafka-logging-sidecar
  name: kafka-logging-sidecar
  resources: {}
  env:
    - name: PROCESS_GREP_REGEX
      value: "[j]ava"
    - name: KAFKA_TOPIC
        value: myTopic
    - name: KAFKA_SERVER
        value: http://kafka:9091
  volumeMounts:
    - mountPath: /home/one/logs
      name: log-path
```

## Read from File, write to kafka
```
- image: ykorzikowski/kafka-logging-sidecar
  name: kafka-logging-sidecar
  env:
    - name: LOGFILE
        value: /home/phoenix/logs/app.log
    - name: KAFKA_TOPIC
        value: myTopic
    - name: KAFKA_SERVER
        value: http://kafka:9091
  volumeMounts:
    - mountPath: /home/phoenix/logs
        name: log-path
```

## Read from file, prettify only
```
- image: ykorzikowski/kafka-logging-sidecar
  name: kafka-logging-sidecar
  env:
    - name: LOGFILE
        value: /home/phoenix/logs/app.log
  volumeMounts:
    - mountPath: /home/phoenix/logs
        name: log-path
```