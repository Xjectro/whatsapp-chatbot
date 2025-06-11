from flask import Flask
from .config import Config
from .routes import register_routes


app = Flask(__name__)
app.config.from_object(Config)

register_routes(app)

app.run(debug=False)
