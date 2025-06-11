import google.generativeai as genai
from app.config import Config

genai.configure(api_key=Config.gemini_api_key)
model = genai.GenerativeModel("gemini-1.5-flash")


def generate_message(question):
    try:
        result = model.generate_content(question)
        return result.text
    except Exception as e:
        raise
