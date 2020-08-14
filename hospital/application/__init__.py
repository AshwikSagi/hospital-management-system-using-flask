from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)


app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'


app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////Users/SHRUTI PETWAL/Desktop/hospital/database.db'

db=SQLAlchemy(app)
db.init_app(app)



from application import routes



