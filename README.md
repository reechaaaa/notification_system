# Notification Service

A Python FastAPI microservice for queuing and delivering notifications (email, SMS, in-app) using RabbitMQ and MongoDB.

---

## Features
- **REST API** to queue and retrieve notifications
- **Notification types:** `email`, `sms`, `in_app` 
- **RabbitMQ** for message queuing
- **MongoDB** for notification storage
- **Exponential backoff** retry logic for delivery failures

---

## Folder Structure
```
notification-service/
├── app/
│   ├── api.py
│   ├── db.py
│   ├── main.py
│   ├── notifier.py
│   ├── schemas.py
│   └── workers.py
├── queue/
│   ├── consumer.py
│   └── producer.py
├── requirements.txt
└── .env
```

---

## Prerequisites
- Python 3.10+
- RabbitMQ running locally (default port 5672) or using docker.
- MongoDB running locally (default port 27017)

---

## Setup

1. **Clone the repository**
    Create an environment in terminal
        python -m venv venv
        .\venv\Scripts\activate

2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

3. **Create a `.env` file** in the project root:
   ```ini
   MONGO_URI=mongodb://localhost:27017
   RABBITMQ_HOST=localhost
   ```

4. **Start RabbitMQ and MongoDB**
   - On windows (RabbitMQ via Docker)
   - Connect with MongoDb Compass

---

## Running the Application

### 1. Start the FastAPI server
```sh
uvicorn app.main:app --reload
```
- The API will be available at [http://localhost:8000](http://localhost:8000)

### 2. Start the RabbitMQ consumer (in a separate terminal inside environment)
```sh
python queue/consumer.py
```

---

## API Usage (Can use postman)

### Queue a Notification
```sh
curl -X POST http://localhost:8000/notifications \
  -H "Content-Type: application/json" \
  -d '{"user_id": "user123", "type": "email", "message": "Hello from FastAPI!"}'
```

### Queue an SMS Notification
```sh
curl -X POST http://localhost:8000/notifications \
  -H "Content-Type: application/json" \
  -d '{"user_id": "user456", "type": "sms", "message": "Your OTP is 123456."}'
```

### Queue an In-App Notification
```sh
curl -X POST http://localhost:8000/notifications \
  -H "Content-Type: application/json" \
  -d '{"user_id": "user789", "type": "in_app", "message": "You have a new message!"}'
```

### Retrieve Notifications for a User
```sh
curl http://localhost:8000/users/user123/notifications
```







