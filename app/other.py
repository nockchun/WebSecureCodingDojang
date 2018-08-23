#-*- encoding: utf-8 -*-
import os
from flask import Flask, Blueprint, current_app, render_template, jsonify, request
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from app import appcontext as ctx

other = Blueprint("other", __name__, template_folder='templates', url_prefix="/other")

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

@other.route('/init_db', methods=['GET'])
def init_db():
	project_dir = os.path.dirname(os.path.abspath(__file__))
	database_file = os.path.join(project_dir, "../secorecoding.db")
	if os.path.exists(database_file):
		os.remove(database_file)

	ctx.db.create_all()
	admin = ctx.User("admin", "admin", "admin@localhost.local", "coding", "secure")
	ctx.db.session.add(admin)
	ctx.db.session.commit()
	return render_template("dashboard.html")

# Bypass Field Form
class BypassFieldForm(Form):
	email = StringField("email")
	disabledinput = StringField("disabledinput", [validators.Length(min=4, max=25)])
	selectcoupon = StringField("selectcoupon")
	radiocoupon = StringField("radiocoupon")
	checkmeout = BooleanField("checkmeout")

@other.route('/bypass_field', methods=['GET', 'POST'])
def bypass_field():
	form = BypassFieldForm(request.form)
	return render_template("bypass_field.html", form=form)
