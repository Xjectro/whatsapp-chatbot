from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
    TWILIO_FROM = os.getenv("TWILIO_FROM")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
