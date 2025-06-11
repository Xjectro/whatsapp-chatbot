from twilio.rest import Client
from app.config import Config

client = Client(Config.twilio_account_sid, Config.twilio_auth_token)


def send_message(body: str, to: str):
    client.messages.create(from_=Config.twilio_from, body=body, to=to)
