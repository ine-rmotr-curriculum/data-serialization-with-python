#!/usr/bin/env python
from sys import stderr
import socket
from random import choice, random
from hashlib import md5
from threading import Thread
from pathlib import Path
from time import sleep
from flask import Flask, jsonify, request, Response

app = Flask(__name__)
port = 2552

greetings = Path('greetings.txt').read_text().splitlines()
names = Path('names.txt').read_text().splitlines()

@app.route('/stream')
def streamed_response():
    def generate():
        while True:
            greet = choice(greetings)
            name = choice(names)
            yield f"{greet} {name}!"
            sleep(random())
    return Response(generate(), mimetype='text/plain')         

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
    sleep(0.5)  # Give thread a moment to launch
