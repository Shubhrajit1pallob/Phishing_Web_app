from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv("/Users/shawn47/Documents/Python_Projects/.env")

def create_app():
    app = Flask(__name__)

    from .routes import main
    app.register_blueprint(main)

    return app