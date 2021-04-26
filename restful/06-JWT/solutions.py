#!/usr/bin/env python
from datetime import datetime, timedelta
from random import shuffle
from flask import Flask, abort, jsonify, request, make_response
import requests
import jwt
import zen
app = Flask(__name__)

keyserver = "http://localhost:5010/getkey"
server2_private_key = open('server2.key').read()
server2_public_key = open('server2.key.pub').read()

@app.route('/login', methods=['POST'])
def login():
    payload = jwt.decode(request.data, verify=False)
    user = payload.get('iss')
    resp = requests.get(f"{keyserver}?identity={user}")
    # Check if this is name of real user
    if resp.status_code != 200:
        abort(401)
    # Now find out if token really came from claimed user
    try:
        pubkey = resp.text
        jwt.decode(request.data, pubkey, algorithm="RS256")
        nbf = datetime.utcnow() + timedelta(seconds=10)
        exp = datetime.utcnow() + timedelta(seconds=30)

        token = jwt.encode({'nbf': nbf, 'exp': exp},
                           server2_private_key, algorithm="RS256")
        resp = make_response(token)
        resp.mimetype = "application/jwt"
        return resp
    except Exception as err:
        return make_response(str(err), 403)

@app.route('/', methods=['POST'])
def q():
    # Have I received a valid token I issues?
    try:
        jwt.decode(request.data, server2_public_key, algorithm="RS256")
        shuffle(zen.lines)
        return make_response(zen.lines[-1])
    except Exception as err:
        return make_response(str(err), 403)

if __name__ == "__main__":
    app.run(port=5025)
