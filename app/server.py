from mongoengine import *
from flask import Flask
from app.auth import auth


def create_app():
    app = Flask(__name__)

    app.register_blueprint(auth, url_prefix='/')

    cloud_uri = ('mongodb+srv://ifunanyasunday7:'
                 '58tnZeQYOUBG7nQt@wemen-dev.esx5cjc.mongodb.net/?retryWrites=true&w=majority')

    connect(host=cloud_uri)
    app.config['SECRET_KEY'] = 'secretkey'

    return app
