def send_email(user_id: str, message: str):
    print(f"[EMAIL] Sent to {user_id}: {message}")
    return True

def send_sms(user_id: str, message: str):
    print(f"[SMS] Sent to {user_id}: {message}")
    return True

def send_in_app(user_id: str, message: str):
    print(f"[IN_APP] Sent to {user_id}: {message}")
    return True

def send_notification(notification_type: str, user_id: str, message: str):
    if notification_type == "email":
        return send_email(user_id, message)
    elif notification_type == "sms":
        return send_sms(user_id, message)
    elif notification_type == "in_app":
        return send_in_app(user_id, message)
    else:
        raise ValueError("Unknown notification type") 