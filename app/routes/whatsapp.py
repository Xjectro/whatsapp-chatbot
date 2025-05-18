from flask import Blueprint, request
from twilio.rest import Client
from app.config import Config
from app.services.chatbot import generate_message
from app.services.twilio import send_message

bp = Blueprint("whatsapp", __name__)
client = Client(Config.TWILIO_ACCOUNT_SID, Config.TWILIO_AUTH_TOKEN)


@bp.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.values.get("Body", "").strip()
    from_number = request.values.get("From", "")
    message = generate_message(incoming_msg)
    send_message(body=message, to=from_number)
    return "", 200
