from flask import Flask
from config import configs
from flask_bootstrap import Bootstrap

# from newsapi import NewsApiClient

app = Flask(__name__,instance_relative_config = True)
bootstrap = Bootstrap()

def create_app(config_name):
	# Initializing application
	app.config.from_object(configs[config_name])
	bootstrap.init_app(app)

	
	from . requests import config_request
	config_request(app)
	return app



# # Setting up configuration

# app.config.from_pyfile('config.py')
# # Initializing Flask Extensions

# #init
# # newsapi = NewsApiClient(api_key=)

# from app import app

from app import app