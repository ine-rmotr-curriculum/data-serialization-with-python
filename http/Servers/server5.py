#!/usr/bin/env python
from flask import Flask, jsonify, request, abort
app = Flask(__name__)


@app.route('/hello')
def hello():
    return "Hello"


@app.route('/notfound')
def notfound():
    return abort(404)


@app.route('/json', methods=["GET", "POST", "PUT"])
def json():
    if request.method in {"PUT", "POST"}: 
        resp = dict(request.form)
    else:
        resp = dict(request.args)
    resp['Server'] = "Test Server"
    return jsonify(resp)


if __name__ == '__main__':
    # Expose to all external-facing IP addresses
    from werkzeug.serving import WSGIRequestHandler
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run(host='0.0.0.0', port=2505)

