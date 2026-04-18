import pika
import time
import random

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()
channel.queue_declare(queue="letterbox")

message_cnt = 1

while True:
    message = f"Sending Message {message_cnt}"
    channel.basic_publish(exchange="", routing_key="letterbox", body=message)
    print(f"Sent: {message}")
    time.sleep(random.randint(1, 3))
    message_cnt += 1