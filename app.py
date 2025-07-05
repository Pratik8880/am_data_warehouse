from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)         #Create a flask app instance 
app.config.from_object('config')    #loads config from config file 
db = SQLAlchemy(app)         # link to flask app 
