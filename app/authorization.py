#-*- encoding: utf-8 -*-
from flask import Flask, Blueprint, current_app, render_template, jsonify, request
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from app import appcontext as ctx

authorization = Blueprint("member", __name__, template_folder='templates', url_prefix="/authorization")

# Bypass Field Form
class BypassFieldForm(Form):
	email = StringField("email")
	disabledinput = StringField("disabledinput", [validators.Length(min=4, max=25)])
	selectcoupon = StringField("selectcoupon")
	radiocoupon = StringField("radiocoupon")
	checkmeout = BooleanField("checkmeout")

@authorization.route('/myinfo', methods=['GET', 'POST'])
def myinfo():
	username = request.cookies.get("sc_u")
	### vulnerable
	sql = """
		SELECT *
		  FROM user
		 WHERE username = '{}'
	""".format(username)
	result = ctx.db.engine.execute(sql).fetchone()

	return render_template("myinfo.html", user=result)
