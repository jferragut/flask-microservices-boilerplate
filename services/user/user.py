import os
from flask import Flask, request, jsonify, url_for, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from services.user.model import db
from services.user.model import User

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.update(
    SQLALCHEMY_DATABASE_URI=os.environ.get('DB_CONNECTION_STRING'),
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)
MIGRATE = Migrate(app, db)
db.init_app(app)
with app.app_context():
    db.create_all()
    db.session.commit()
CORS(app)


# simple hello
@app.route('/')
def main():
    return "hello, world."


@app.route('/user', methods=["GET", "POST"])
def user():
    if request.method == 'POST':
        request_json = request.get_json()
        name = request_json.get('username')
        email = request_json.get('email')
        new = User(username=name, email=email)
        db.session.add(new)
        db.session.commit()
        return 'User Added',200
    else:
        return jsonify(json_list=[i.serialize for i in User.query.all()]), 200


# this only runs if `$ python src/main.py` is exercuted
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT)

