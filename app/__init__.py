#coding=utf-8
from flask import Flask

from config import config
from flask_sqlalchemy import SQLAlchemy
#from flask.ext.pymongo import PyMongo
from flask_mongoengine import MongoEngine
from flask_pymongo import PyMongo
from flask_login import LoginManager
from models import User
#mongo=PyMongo()
db = SQLAlchemy()
mongo = MongoEngine()
login_manager = LoginManager()

def create_app(config_name='dev'):
	app=Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)
	#app.config["MONGO_URI"] = "mongodb://localhost:27017/"
	#mongo=PyMongo()
	db.init_app(app)
	mongo.init_app(app)

	login_manager.init_app(app)
	login_manager.login_view = 'users.login'
	login_manager.login_message ='请登录'

	from main import main as main_blueprint
	app.register_blueprint(main_blueprint)
	

	from api import api as api_blueprint
	app.register_blueprint(api_blueprint)

	return app

