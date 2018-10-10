#-*- encoding: utf-8 -*-
import os
from pathlib import Path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app():
	app = Flask(__name__)

	from .home import home
	from .authentication import authentication
	from .other import other
	from .authorization import authorization
	app.register_blueprint(home)
	app.register_blueprint(authentication)
	app.register_blueprint(authorization)
	app.register_blueprint(other)

	app.secret_key = "secure coding"

	return app

app = create_app()

def create_db():
	project_dir = os.path.dirname(os.path.abspath(__file__))
	database_file = os.path.join(project_dir, "../secorecoding.db")
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
	app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///{}".format(database_file)
	db = SQLAlchemy(app)

	return db

db = create_db()

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), nullable=False)
	password = db.Column(db.String(80), nullable=False)
	email = db.Column(db.String(120))
	firstname = db.Column(db.String(80))
	lastname = db.Column(db.String(80))


	def __init__(self, username, password, email, firstname, lastname):
		self.username = username
		self.password = password
		self.email = email
		self.firstname = firstname
		self.lastname = lastname

	def __repr__(self):
		return "[User > id:{}, pass:{}, email:{}, first:{}, last:{}]" \
			.format(self.username, self.password, self.email, self.firstname, self.lastname)

