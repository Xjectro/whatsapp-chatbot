# WhatsApp Chatbot 🤖💬

Chatbot project delivering an AI-powered WhatsApp chat experience. Uses the Gemini AI model and Twilio API to provide real-time, intelligent responses.

## ⚙️ Features
- AI-powered conversation 🧠  
- WhatsApp integration via Twilio 📲  
- Easy configuration 🔧  
- Error handling & logging 📝  

## 📋 Prerequisites
- Python 3.8 or higher 🐍  
- Twilio account & WhatsApp-enabled number 📞  
- OpenAI API key 🔑  

## 🚀 Installation
```powershell
git clone https://github.com/Xjectro/whatsaap-chatbot.git
cd whatsaap-chatbot
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## 🔧 Configuration
Update the variables in `app/config.py`:
```python
GEMINI_API_KEY   = "your_gemini_ai_key"
TWILIO_ACCOUNT_SID = "your_twilio_sid"
TWILIO_AUTH_TOKEN = "your_twilio_token"
TWILIO_WHATSAPP_NUMBER = "whatsapp:+1234567890"
```

## 🏃 Usage
```powershell
python -m app
```
Webhook URL:
```
POST https://<your_server_address>/whatsapp
```

## 🗂️ Project Structure
- `app/`
  - `__init__.py`       : Application entry point  
  - `config.py`         : Configuration variables  
  - `routes/`
    - `whatsapp.py`     : Webhook route  
  - `services/`
    - `chatbot.py`      : OpenAI integration  
    - `twillio.py`      : Twilio messaging  
- `requirements.txt`    : Dependencies  
- `Makefile`            : Helper commands  

## 🤝 Contributing
Bug reports, ideas, or pull requests are welcome. Let's build together! 🌟

## 📝 License
This project is licensed under the MIT License.  
© 2025
