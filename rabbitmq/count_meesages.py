# import rabbitpy
#
# with rabbitpy.Connection('amqps://multiply-rapid-polecat:gjnR9SRJ7YpMWoWTNq87pw1S@b-6d608ba4-94db-495c-b8c9'
#                          '-81bf3d9dcc05.mq.us-east-1.amazonaws.com:5671') as conn:
#     with conn.channel() as channel:
#         queue = rabbitpy.Queue(channel, 'test')
#         print('The queue has {0} messages'.format(len(queue)))


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


# def check_messages_in_all_queue(host):
#     try:
#         logging.info(f"Connecting to RabbitMQ instance '{host}'...")
#         connection = pika.BlockingConnection(pika.ConnectionParameters(host))
#         channel = connection.channel()
#         queues = channel.queue_declare(queue='', passive=True, durable=True, exclusive=False, auto_delete=False)
#
#         for queue in queues:
#             count = queue.message_count
#             if count > 1000:
#                 logging.warning(f"Queue '{queue.name}' has exceeded 1000 messages. Current count: {count}")
#                 # send_slack_notification(host, queue.name, count)
#             else:
#                 logging.info(f"Queue '{queue.name}'")
#                 # (f"Queue '{queue.name}' has exceeded 1000 messages. Current count: {count}")



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
            client_url = f"https://{host}/queues/{queue}"
            description = f"Queue {queue} on host {host} has exceeded 1000 messages"
            trigger_pagerduty(service_key, "trigger", description, client, client_url)
        logging.info(f"Host: {host}, Queue: {queue}, Messages: {message_count}")
    except:
        logging.error(f"Failed to connect to host {host}")


# hosts=
# hosts = os.getenv("HOSTS").split(",")
queue = os.getenv("QUEUE")


# for host in hosts:
#     check_messages_in_queue(host, queue)