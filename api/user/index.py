import os
from flask import Flask, request, jsonify, url_for, Blueprint, Response
# from flask_dotenv import DotEnv
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
# from api.user.model import db,User


app = Flask(__name__)
# app.url_map.strict_slashes = False
# app.config.from_pyfile('settings.cfg')
# MIGRATE = Migrate(app, db)
# db.init_app(app)
# with app.app_context():
#     db.create_all()
#     db.session.commit()
# CORS(app)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return Response("<h1>Flask on Now</h1><p>You visited: /%s</p>" % (path), mimetype="text/html")


# @app.route('/api/user/', methods=["GET", "POST"])
# def user():
#     if request.method == 'POST':
#         request_json = request.get_json()
#         name = request_json.get('username')
#         email = request_json.get('email')
#         new = User(username=name, email=email)
#         db.session.add(new)
#         db.session.commit()
#         return 'User Added',200
#     else:
#         json_list = [i.serialize for i in User.query.all()]
#         return jsonify(json_list), 200

