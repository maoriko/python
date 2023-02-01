import pika
import os
import requests
import logging

# set up logging
logging.basicConfig(filename="rabbitmq_message_checker.log", level=logging.INFO,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

# set up PagerDuty API endpoint
PAGERDUTY_API_URL = "https://events.pagerduty.com/v2/enqueue"


def trigger_pagerduty(service_key, event_type, description, client, client_url):
    payload = {
        "routing_key": service_key,
        "event_action": event_type,
        "dedup_key": client,
        "payload": {
            "summary": description,
            "source": client,
            "severity": "critical",
            "component": client_url,
        }
    }
    headers = {
        "Accept": "application/vnd.pagerduty+json;version=2",
        "Content-Type": "application/json"
    }
    response = requests.post(PAGERDUTY_API_URL, json=payload, headers=headers)
    if response.status_code == 202:
        logging.info("PagerDuty incident created successfully")
    else:
        logging.error("Failed to create PagerDuty incident")


def get_rabbitmq_queues(host):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
    channel = connection.channel()
    queues = channel.queue_declare(passive=True)
    queue_names = [queue.queue for queue in queues]
    connection.close()
    return queue_names


def check_messages_in_queue(host, queue):
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host))
        channel = connection.channel()
        queue_info = channel.queue_declare(queue, passive=True)
        message_count = queue_info.method.message_count
        if message_count > 1000:
            # trigger PagerDuty incident
            service_key = os.getenv("PAGERDUTY_SERVICE_KEY")
            client = "RabbitMQ"
            client_url = f"{host}/queues/{queue}"
            description = f"Queue {queue} on host {host} has exceeded 1000 messages"
            trigger_pagerduty(service_key, "trigger", description, client, client_url)
        logging.info(f"Host: {host}, Queue: {queue}, Messages: {message_count}")
    except:
        logging.error(f"Failed to connect to host {host}")


def main():
    # hosts = ["host1", "host2", "host3"]
    hosts = os.getenv("HOSTS").split(",")
    for host in hosts:
        queue_names = get_rabbitmq_queues(host)
        for queue_name in queue_names:
            print(queue_name, host)
            check_messages_in_queue(host, queue_name)

# hosts = os.getenv("HOSTS").split(",")
# hosts = ["host1", "host2", "host3"]
# queue_name = "queue_name"
