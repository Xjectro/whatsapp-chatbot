from twilio.rest import Client
from app.config import Config

client = Client(Config.TWILIO_ACCOUNT_SID, Config.TWILIO_AUTH_TOKEN)


def send_message(body: str, to: str):
    client.messages.create(from_=Config.TWILIO_FROM, body=body, to=to)
