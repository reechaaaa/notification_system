from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime

class NotificationCreate(BaseModel):
    user_id: str
    type: Literal["email", "sms", "in_app"]
    message: str

class Notification(NotificationCreate):
    id: str = Field(..., alias="_id")
    status: str
    created_at: datetime 