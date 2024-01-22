from mongoengine import *
from flask import Flask
from app.auth import auth
import os
from dotenv import load_dotenv


def create_app():
    app = Flask(__name__)

    app.register_blueprint(auth, url_prefix='/')
    
    load_dotenv()
    mongodb_uri = os.environ['dbase_uri']
    
    connect(host=mongodb_uri)
    
    

    return app
