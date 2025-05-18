import pika
import os
from dotenv import load_dotenv

load_dotenv()
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")

def publish_message(message: str):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
    channel = connection.channel()
    channel.queue_declare(queue="notifications")
    channel.basic_publish(exchange="", routing_key="notifications", body=message)
    connection.close()

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        publish_message(sys.argv[1])
    else:
        print("Usage: python producer.py '<json_message>'") 