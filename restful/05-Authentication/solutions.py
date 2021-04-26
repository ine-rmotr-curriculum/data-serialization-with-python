#!/usr/bin/env python
import secrets
from random import randint
from datetime import datetime
from flask import Flask, request, make_response, jsonify
app = Flask(__name__)

# User/password pairs
authorized = {'Alice': 'alice_pw', 
              'Bob': 'bob_pw', 
              'Carlos': 'carlos_pw',
              'Diane': 'diane_pw',
              'Eshana': 'eshana_pw'}

auth_tokens = dict()
usage_count = dict()

@app.route('/login', methods =['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Fail in slightly different ways under different bad logins
    if not username or not password:
        hdr = {'WWW-Authenticate' : 'Basic realm="Login required"'}
        return make_response('Verification failed', 401, hdr)
    
    elif username not in authorized:
        hdr = {'WWW-Authenticate' : 'Basic realm="No such user"'}
        return make_response('Verification failed', 401, hdr)
    
    elif password != authorized[username]:
        hdr = {'WWW-Authenticate' : 'Basic realm="Password incorrect"'}
        return make_response('Verification failed', 403, hdr)
    
    else:
        token = secrets.token_urlsafe(16)
        auth_tokens[username] = token
        resp = make_response("Logged in", 200)
        resp.set_cookie('app1-username', username)
        resp.set_cookie('app1-token', token)
        resp.set_cookie('app1-login-timestamp', datetime.now().isoformat())
        return resp

@app.route('/limited-info')
def limited_info():
    username = request.cookies.get('app1-username')
    token = request.cookies.get('app1-token', object())
    if token != auth_tokens.get(username):
        return make_response(f"{username} denied access to resource", 403)
    uses = usage_count.get(username, 0)
    if uses >= 3:
        del auth_tokens[username]
        del usage_count[username]
        return make_response(f"{username} denied access to resource", 403)
    else:
        usage_count[username] = uses+1
    return jsonify({f"{username} favorite number": randint(1, 100)})
    
    
if __name__ == "__main__":
    app.run(ssl_context=('pubkey.pem', 'private.pem'), port=5015)