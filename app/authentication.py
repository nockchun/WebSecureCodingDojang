#-*- encoding: utf-8 -*-
from flask import Flask, Blueprint, current_app, render_template, jsonify, request, redirect, make_response 
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from app import appcontext as ctx

authentication = Blueprint("authentication", __name__, template_folder='templates')

# Login ----------------------------------------------------------------------------
@authentication.route('/login', methods=['GET'])
def login():
	salutation = 'Thank for using flask-fundamentum!'
	return render_template("login.html")

class LoginForm(Form):
	inputUsername = StringField("inputUsername")
	inputPassword = StringField("inputPassword")

@authentication.route('/login_do', methods=['POST'])
def loginDo():
	form = LoginForm(request.form)

	### vulnerable
	sql = """
		SELECT *
		  FROM user
		 WHERE username = '{}'
		   AND password = '{}'
	""".format(form.inputUsername.data, form.inputPassword.data)
	result = ctx.db.engine.execute(sql).fetchall()

	if (len(result) > 0):
		resp = make_response(render_template("myinfo.html", user=result[0]))
		resp.set_cookie("sc_u", form.inputUsername.data)
		return resp
	return render_template("login.html")

# Regist Member --------------------------------------------------------------------
@authentication.route('/register', methods=['GET'])
def register():
	return render_template("register.html")

class RegistMemberForm(Form):
	inputUsername = StringField("inputUsername")
	inputPassword = StringField("inputPassword")
	confirmPassword = StringField("confirmPassword")
	firstName = StringField("firstName")
	lastName = StringField("lastName")
	inputEmail = StringField("inputEmail")

@authentication.route('/register_do_add', methods=['POST'])
def registerDoAdd():
	form = RegistMemberForm(request.form)

	### vulnerable
	sql = """
		INSERT INTO user(username, password, email, firstname, lastname)
		VALUES ('{}', '{}', '{}', '{}', '{}')
	""".format(form.inputUsername.data, form.inputPassword.data, form.inputEmail.data, form.firstName.data, form.lastName.data)
	ctx.db.engine.execute(sql)

	### not vulnerable
	# newUser = ctx.User(form.inputUsername.data, form.inputPassword.data, form.inputEmail.data, form.firstName.data, form.lastName.data)
	# ctx.db.session.add(newUser)
	# ctx.db.session.commit()
	# current_app.logger.info('New User Added: %s', (newUser))

	return render_template("login.html")

# Logout ---------------------------------------------------------------------------
@authentication.route('/logout', methods=['GET'])
def logout():
	# current_app.logger.info('Resource requested: %s', ('welcome'))
	salutation = 'Thank for using flask-fundamentum!'
	return render_template("dashboard.html", msg=salutation)
