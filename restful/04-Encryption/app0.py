#!/usr/bin/env python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Secret Message!"

if __name__ == "__main__":
    app.run(port=5000)