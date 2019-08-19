from flask import jsonify

from app.api.home import home

@home.route('')
def index():
    return jsonify(hello='world')