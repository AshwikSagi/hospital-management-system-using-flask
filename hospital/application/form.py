from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,SelectField,FloatField,IntegerField
from wtforms.validators import InputRequired, DataRequired, Email, Length, EqualTo, ValidationError
from werkzeug.security import generate_password_hash, check_password_hash
from application import db
from wtforms.fields.html5 import DateField
import flask,sqlite3
from flask_login import LoginManager, UserMixin, login_user
import string


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=6, max=18)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6, max=15)])
    submit=SubmitField("Login")

class DeleteForm(FlaskForm):
	pid=StringField("Patient SSN ID",validators=[DataRequired(), Length(min=9,max=9)])
	name=StringField("Name",validators=[DataRequired(), Length(min=7,max=40)])
	age=StringField("Age",validators=[DataRequired(), Length(min=1,max=3)])
	doa=DateField('Date of admission',format= '%Y-%m-%d', validators=[DataRequired()])
	get=SubmitField("Get")
	tob=SelectField("Type of bed",
	choices=[("Single","Single"), ("Semi Sharing","Semi Sharing"), ("General", "General")], validators=[DataRequired()])
	address=StringField("Address",validators=[DataRequired(), Length(min=10,max=100)])
	state=SelectField('State',
        choices=[("Andhra Pradesh", "Andhra Pradesh"), ("Telangana", "Telangana"), ("Karnataka","Karnataka"), ("Maharashtra", "Maharashtra")], validators=[DataRequired()])
	city=SelectField ("City",
		choices=[("Hyderabad", "Hyderabad"), ("Amravati", "Amravati"), ("Bangalore", "Bangalore"), ("Mumbai", "Mumbai"), ("Nagpur", "Nagpur"),("Pune", "Pune"), ("Vishakhapatnam", "Vishakhapatnam")], validators=[DataRequired()])
	submit=SubmitField("Delete")

class DelForm(FlaskForm):
	pid=StringField("Patient SSN ID",validators=[DataRequired(),Length(min=9,max=9)])
	get=SubmitField("Get")

class IssueForm(FlaskForm):
	submit=SubmitField("Issue Medicines")

class FindmedsForm(FlaskForm):
	name=StringField("Medicine name",validators=[DataRequired(),Length(min=6,max=40)])
	qty=FloatField("Quantity required", validators=[DataRequired()])
	add=SubmitField("Add medicine")
	update=SubmitField("Buy medicines")

class CreateForm(FlaskForm):
	pid=StringField("Patient SSN ID",validators=[DataRequired(), Length(min=9,max=9)])
	name=StringField("Name",validators=[DataRequired(), Length(min=7,max=40)])
	age=StringField("Age",validators=[DataRequired(), Length(min=1,max=3)])
	doa=DateField('Date of admission',format= '%Y-%m-%d', validators=[DataRequired()])
	tob=SelectField("Type of bed",
	choices=[("Single","Single"), ("Semi Sharing","Semi Sharing"), ("General", "General")], validators=[DataRequired()])
	address=StringField("Address",validators=[DataRequired(), Length(min=10,max=100)])
	state=SelectField('State',
        choices=[("Andhra Pradesh", "Andhra Pradesh"), ("Telangana", "Telangana"), ("Karnataka","Karnataka"), ("Maharashtra", "Maharashtra")], validators=[DataRequired()])
	city=SelectField ("City",
		choices=[("Hyderabad", "Hyderabad"), ("Amravati", "Amravati"), ("Bangalore", "Bangalore"), ("Mumbai", "Mumbai"), ("Nagpur", "Nagpur"),("Pune", "Pune"), ("Vishakhapatnam", "Vishakhapatnam")], validators=[DataRequired()])
	submit=SubmitField("Create")
	
class SeaForm(FlaskForm):
	pid=StringField("Patient ID",validators=[DataRequired(),Length(min=9,max=9)])
	get=SubmitField("get")
	
	
class SearchForm(FlaskForm):
	pid=StringField("Patient ID",validators=[DataRequired(),Length(min=9,max=9)])
	get=SubmitField("get")
	name=StringField("Name",validators=[DataRequired(),Length(min=7,max=40)])
	age=StringField("Age",validators=[DataRequired(),Length(min=1,max=3)])
	doa=DateField('Date of admission',format= '%Y-%m-%d', validators=[DataRequired()])
	tob=StringField("Type of bed")
	address=StringField("Address",validators=[DataRequired(), Length(min=10,max=100)])
	state=StringField('State')
	city=StringField ("City")

class UpdateForm(FlaskForm):
	pid=StringField("Patient ID",validators=[DataRequired(),Length(min=9,max=9)])
	name=StringField("Name",validators=[DataRequired(),Length(min=7,max=40)])
	age=StringField("Age",validators=[DataRequired(),Length(min=1,max=3)])
	doa=DateField('Date of admission',format= '%Y-%m-%d', validators=[DataRequired()])
	tob=SelectField("Type of bed",
	choices=[("Single","Single"), ("Semi Sharing","Semi Sharing"), ("General", "General")], validators=[DataRequired()])
	address=StringField("Address",validators=[DataRequired(), Length(min=10,max=100)])
	state=SelectField('State',
        choices=[("Andhra Pradesh", "Andhra Pradesh"), ("Telangana", "Telangana"), ("Karnataka","Karnataka"), ("Maharashtra", "Maharashtra")], validators=[DataRequired()])
	city=SelectField ("City",
		choices=[("Hyderabad", "Hyderabad"), ("Amravati", "Amravati"), ("Bangalore", "Bangalore"), ("Mumbai", "Mumbai"), ("Nagpur", "Nagpur"),("Pune", "Pune"), ("Vishakhapatnam", "Vishakhapatnam")], validators=[DataRequired()])
	submit=SubmitField("Update")
	
	
class UpForm(FlaskForm):
	pid=StringField("Patient ID",validators=[DataRequired(),Length(min=9,max=9)])
	get=SubmitField("get")
