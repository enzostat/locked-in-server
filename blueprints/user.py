from flask import Blueprint, render_template, request, redirect
from datetime import datetime
from bson.objectid import ObjectId

user_blueprint = Blueprint('characters', __name__, url_prefix='/characters')


@user_blueprint.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'GET':
        return 'Welcome to Hell'