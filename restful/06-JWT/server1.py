#!/usr/bin/env python
from flask import Flask, abort, jsonify, request, make_response
import requests
import jwt
app = Flask(__name__)

keyserver = "http://localhost:5010/getkey"

@app.route('/', methods=['POST'])
def query():
    # Look at content without verification first
    payload = jwt.decode(request.data, verify=False)
    
    # Find the public key for the requester
    resp = requests.get(f"{keyserver}?identity={payload['iss']}")
    if resp.status_code != 200:
        abort(401)
    
    # We have found a public key, verify now
    pubkey = resp.text
    try:
        verified = jwt.decode(request.data, pubkey, algorithm="RS256")
        # Real code will do something with fields
        query = verified['query']
        iat = verified['iat']
        return jsonify({query: 42})
    except Exception as err:
        return make_response(str(err), 403)

if __name__ == "__main__":
    app.run(port=5005)