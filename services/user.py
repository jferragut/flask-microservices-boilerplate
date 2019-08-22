import os
from flask import Flask, request, jsonify, url_for, Blueprint
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from models import user_model

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, user_model)
user_model.init_app(app)
CORS(app)


# simple hello
@app.route('/')
def sitemap():
    return "hello, world."

@user_blueprint.route('/user', methods=["GET"])
def get_users():
    response_body = {"name": "Jon"}
    return jsonify(response_body), 200

# this only runs if `$ python src/main.py` is exercuted
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT)

