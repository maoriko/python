FROM python:3.8

WORKDIR /app

COPY . /app

RUN pip install pika requests

ENV HOSTS "host1,host2,host3"
ENV QUEUE "queue_name"
ENV PAGERDUTY_SERVICE_KEY "your_pagerduty_service_key"

CMD ["python", "rabbitmq_message_checker.py"]
