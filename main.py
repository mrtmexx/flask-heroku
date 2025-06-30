#!/usr/bin/env python
# coding=utf-8

import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/test")
def test():
    return "Test Page!"

@app.route("/version")
def version():
    return os.environ.get('VERSION', 'UNDEFINED')

if __name__ == '__main__':
    app.run(debug=True)
