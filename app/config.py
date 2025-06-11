from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    twilio_account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    twilio_from = os.getenv("TWILIO_FROM")
    gemini_api_key = os.getenv("GEMINI_API_KEY")
