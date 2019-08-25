from flask import Flask
app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
	return "You visited the %s page" % (path)
