import os
from flask import Flask, request, jsonify, url_for, Blueprint
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from models import user_model

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/user',methods=["GET"])
def user_blueprint():
    userdata = {"name": "Jon"}
    return jsonify(userdata), 200
