import os
from flask import Flask, request, jsonify, url_for, Blueprint

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
	return "You visited the %s page" % (path)