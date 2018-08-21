#-*- encoding: utf-8 -*-
from flask import Flask, Blueprint, current_app, render_template, jsonify

other = Blueprint("other", __name__, template_folder='templates')

@other.route('/error', methods=['GET'])
def error():
	# current_app.logger.info('Resource requested: %s', ('welcome'))
	salutation = 'Thank for using flask-fundamentum!'
	return render_template("error.html", msg=salutation)

@other.route('/noticeboard_list', methods=['GET'])
def noticeboard_list():
	# current_app.logger.info('Resource requested: %s', ('welcome'))
	salutation = 'Thank for using flask-fundamentum!'
	return render_template("noticeboard.html", msg=salutation)

@other.route('/charts', methods=['GET'])
def charts():
	# current_app.logger.info('Resource requested: %s', ('welcome'))
	salutation = 'Thank for using flask-fundamentum!'
	return render_template("charts.html", msg=salutation)
