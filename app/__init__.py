#-*- encoding: utf-8 -*-
from flask import Flask
from app.home import home
from app.authentication import authentication
from app.other import other

app = Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(authentication)
app.register_blueprint(other)
