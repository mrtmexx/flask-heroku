#!/usr/bin/env python
# coding=utf-8

import os
import logging
from flask import Flask

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route("/")
def hello():
    logger.info("Доступ к главной странице /")
    return "Hello World!"

@app.route("/test")
def test():
    return "Test Page!"

@app.route("/version")
def version():
    return os.environ.get('VERSION', 'UNDEFINED')

if __name__ == '__main__':
    app.run(debug=True)
