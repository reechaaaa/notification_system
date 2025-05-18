import pika
import os
import json
import sys
from dotenv import load_dotenv
from tenacity import retry, stop_after_attempt, wait_exponential
# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.workers import process_notification

load_dotenv()
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")

@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=2, max=10))
def handle_message(body):
    data = json.loads(body)
    process_notification(data)

@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=2, max=10))
def connect_to_rabbitmq():
    return pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))

def main():
    try:
        connection = connect_to_rabbitmq()
        channel = connection.channel()
        channel.queue_declare(queue="notifications")

        def callback(ch, method, properties, body):
            try:
                handle_message(body)
                ch.basic_ack(delivery_tag=method.delivery_tag)
            except Exception as e:
                print(f"Failed to process message: {e}")
                ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)

        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue="notifications", on_message_callback=callback)
        print(" [*] Waiting for messages. To exit press CTRL+C")
        channel.start_consuming()
    except pika.exceptions.AMQPConnectionError as e:
        print(f"Failed to connect to RabbitMQ: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 