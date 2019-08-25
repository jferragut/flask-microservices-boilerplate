from flask import Flask

app = Flask(__name__)

@app.route('/test/', defaults={'path': ''})
@app.route('/test/<path:path>')
def catch_all(path):
	return "You visited the %s page" % (path)