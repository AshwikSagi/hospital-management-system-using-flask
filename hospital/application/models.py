import flask,sqlite3
from application import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import LoginManager, UserMixin, login_user
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(18), unique=True)
    password = db.Column(db.String(15))
class Patient(db.Model):
	autopid=db.Column(db.String(9), primary_key=True)
	pid = db.Column(db.String(9), unique=True)
	name = db.Column(db.String(40))
	age = db.Column(db.String(3))
	doa = db.Column(db.Date())
	tob = db.Column(db.String(20))
	address = db.Column(db.String(100))
	state = db.Column(db.String(20))
	city = db.Column(db.String(20))
	status=db.Column(db.String(15))

	

class Medicines(db.Model):
	medid = db.Column(db.String(4), primary_key=True)
	medname = db.Column(db.String(40), unique=True)
	qtyav = db.Column(db.Integer())
	rate = db.Column(db.Float())

class Purdetails(db.Model):
	autoid = db.Column(db.Integer(), primary_key=True) 
	pid = db.Column(db.String(9))
	medid = db.Column(db.String(4))
	medname = db.Column(db.String(40))
	qtypur = db.Column(db.Integer())
	rate = db.Column(db.Float())
	amt = db.Column(db.Float())


class DiagTest(db.Model):
	testid=db.Column(db.String(4),primary_key=True)
	testname=db.Column(db.String(20),unique=True)
	trate=db.Column(db.Float())
class Diagdetails(db.Model):
	did=db.Column(db.String(4), primary_key=True)
	pid = db.Column(db.String(9))
	testid=db.Column(db.String(4))