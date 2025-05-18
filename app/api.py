from fastapi import APIRouter, HTTPException
from app.schemas import NotificationCreate, Notification
from app.db import notifications_collection
import pika
import os
from dotenv import load_dotenv
from bson import ObjectId
from datetime import datetime

load_dotenv()

router = APIRouter()

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")

@router.post("/notifications")
def queue_notification(notification: NotificationCreate):
    # Publish to RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
    channel = connection.channel()
    channel.queue_declare(queue="notifications")
    channel.basic_publish(
        exchange="",
        routing_key="notifications",
        body=notification.json()
    )
    connection.close()
    return {"message": "Notification queued"}

@router.get("/users/{user_id}/notifications", response_model=list[Notification])
def get_user_notifications(user_id: str):
    notifications = list(notifications_collection.find({"user_id": user_id}))
    for n in notifications:
        n["_id"] = str(n["_id"])
    return notifications 