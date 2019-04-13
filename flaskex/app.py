import os
import logging
import socket
from flask import Flask, jsonify

from flaskex.db import db

HOST_NAME = os.environ.get('OPENSHIFT_APP_DNS', 'localhost')
APP_NAME = os.environ.get('OPENSHIFT_APP_NAME', 'flask')
IP = os.environ.get('OPENSHIFT_PYTHON_IP', '127.0.0.1')
PORT = int(os.environ.get('OPENSHIFT_PYTHON_PORT', 5000))
HOME_DIR = os.environ.get('OPENSHIFT_HOMEDIR', os.getcwd())

log = logging.getLogger(__name__)
app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({
        'host_name': HOST_NAME,
        'app_name': APP_NAME,
        'ip': IP,
        'port': PORT,
        'home_dir': HOME_DIR,
        'host': socket.gethostname()
    })


@app.route('/test')
def hello():
    return "Hello World"


@app.route('/customers')
@app.route('/customers/<customer_id>')
def get_customers(customer_id=None):
    if not customer_id:
        response = db.query_db('select * from customers')
    else:
        response = db.query_db(f'select * from customers where CustomerId = {customer_id}')
    return jsonify(response)


if __name__ == '__main__':
    app.run()
