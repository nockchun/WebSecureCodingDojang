#-*- encoding: utf-8 -*-
import os
from pathlib import Path
from app import app

def create_db():
	project_dir = os.path.dirname(os.path.abspath(__file__))
	database_file = os.path.join(project_dir, "../secorecoding.db")
	app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///{}".format(database_file)
	db = SQLAlchemy(app)

	return db

# class User(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	username = db.Column(db.String(80), unique=True, nullable=False)
# 	email = db.Column(db.String(120), unique=True, nullable=False)

# 	def __init__(self, id, username, email):
# 		self.id = id
# 		self.username = username
# 		self.email = email

# 	def __repr__(self):
# 		return '<User %r>' % self.username

# if not Path(database_file).exists():
# 	db.create_all()

db = create_db()