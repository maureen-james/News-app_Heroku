from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap
from newsapi import NewsApiClient

# Initializing application
app = Flask(__name__,instance_relative_config = True)

# Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')
# Initializing Flask Extensions
bootstrap = Bootstrap(app)
#init
# newsapi = NewsApiClient(api_key=)

from app import app