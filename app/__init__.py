from flask import Flask

from app.config import config_env
from app.env import env


app = Flask(__name__)

app.config.from_object(config_env[env])

from app.api.home import home
from app.api.home import controller

app.register_blueprint(home, url_prefix='/')