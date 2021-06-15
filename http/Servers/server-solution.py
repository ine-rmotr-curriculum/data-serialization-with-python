#!/usr/bin/env python
from flask import Flask, jsonify, request, abort
app = Flask(__name__)


@app.route('/hello')
def hello():
    return "Hello"

@app.route('/<path:filepath>')
def get_path(filepath):
    return filepath


if __name__ == '__main__':
    # Expose to all external-facing IP addresses
    from werkzeug.serving import WSGIRequestHandler
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run(host='0.0.0.0', port=2553)

