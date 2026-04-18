import pika
import time
import random

def on_message_received(ch, method, properties, body):
    processing_time = random.randint(1, 6)
    print(f"Received message: {body.decode()} - Processing for {processing_time} seconds")
    time.sleep(processing_time)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print("Done processing message")

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()
channel.queue_declare(queue="letterbox")

# If basic_qos is not set, RabbitMQ will send messages to the next available consumer without waiting for an acknowledgment.
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="letterbox", on_message_callback=on_message_received)

print("Starting to consume messages")
channel.start_consuming()