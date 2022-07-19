FROM python:3.9

RUN mkdir /home/one && useradd -u 1001 -d /home/one one

COPY fetchLogs.sh /home/one
COPY process_logs.py /home/one
COPY requirements.txt /home/one

WORKDIR /home/one

RUN chown -R one /home/one
USER 1001

RUN pip install -r requirements.txt

ENTRYPOINT ["python","process_logs.py"]