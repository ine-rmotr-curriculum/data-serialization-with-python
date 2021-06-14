#!/usr/bin/env python
from sys import stderr
import socket
from hashlib import md5
from threading import Thread
from flask import Flask, jsonify, request, abort

app = Flask(__name__)
port = 2551

@app.route('/hello')
def hello():
    return "Hello"

@app.route('/json', methods=["PUT", "POST"])
def json():
    resp = dict(request.form)
    data = ''.join(resp.values())
    server_name = md5(data.encode()).hexdigest()[:8]
    resp['Server'] = server_name
    return jsonify(resp)

def server():
    app.run(host='0.0.0.0', port=port)

def start():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        if not s.connect_ex(('localhost', port)) == 0:
            t1 = Thread(target=server)
            t1.start()
