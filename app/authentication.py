#-*- encoding: utf-8 -*-
from flask import Flask, Blueprint, current_app, render_template, jsonify

authentication = Blueprint("authentication", __name__, template_folder='templates')

@authentication.route('/login', methods=['GET'])
def login():
	# current_app.logger.info('Resource requested: %s', ('welcome'))
	salutation = 'Thank for using flask-fundamentum!'
	return render_template("login.html", msg=salutation)

@authentication.route('/register', methods=['GET'])
def register():
	# current_app.logger.info('Resource requested: %s', ('welcome'))
	salutation = 'Thank for using flask-fundamentum!'
	return render_template("register.html", msg=salutation)

@authentication.route('/forgot-password', methods=['GET'])
def forgot_password():
	# current_app.logger.info('Resource requested: %s', ('welcome'))
	salutation = 'Thank for using flask-fundamentum!'
	return render_template("forgot-password.html", msg=salutation)

@authentication.route('/logout', methods=['GET'])
def logout():
	# current_app.logger.info('Resource requested: %s', ('welcome'))
	salutation = 'Thank for using flask-fundamentum!'
	return render_template("dashboard.html", msg=salutation)

@authentication.before_request
def before_request():
	print("authentication before_request....!")

@authentication.after_request
def after_request(response):
	print("authentication after_request....!")
