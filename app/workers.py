from app.notifier import send_notification
from app.db import notifications_collection
from datetime import datetime

def process_notification(data: dict):
    user_id = data["user_id"]
    notification_type = data["type"]
    message = data["message"]
    try:
        send_notification(notification_type, user_id, message)
        status = "sent"
    except Exception as e:
        status = f"failed: {str(e)}"
    notifications_collection.insert_one({
        "user_id": user_id,
        "type": notification_type,
        "message": message,
        "status": status,
        "created_at": datetime.utcnow()
    }) 