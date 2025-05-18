import google.generativeai as genai
from app.config import Config

genai.configure(api_key=Config.GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")


def generate_message(question):
    try:
        result = model.generate_content(question)
        return result.text
    except Exception as e:
        return f"Generate message method -> error: {e}"
