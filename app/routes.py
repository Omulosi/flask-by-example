
from flask import Blueprint

bp = Blueprint('routes', __name__)

@bp.route('/')
def hello():
    return "Hello, world!"

@bp.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

