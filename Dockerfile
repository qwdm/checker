FROM python:3.10

COPY config.yml checker.py requirements.txt ./
RUN pip install -r requirements.txt
ENV pushgateway=''
CMD python checker.py
