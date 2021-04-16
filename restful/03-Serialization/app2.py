#!/usr/bin/env python
from flask import Flask, request, jsonify, abort
from bs4 import BeautifulSoup
from striprtf.striprtf import rtf_to_text
app = Flask(__name__)

@app.route('/count-butterflies', methods=["POST"])
def butterfly():
    "Count how many times the word 'butterfly' appears in document"
    document = request.data.decode()  # Make bytes into text
    if request.content_type == 'text/plain':
        text, decoder = document, None
    elif request.content_type == 'text/html':
        soup = BeautifulSoup(document)
        text, decoder = soup.text, "BeautifulSoup"
    elif request.content_type == 'text/rtf':
        text, decoder = rtf_to_text(document), "striprtf"
    else:
        abort(400)  # 400 Bad Request

    count = text.lower().count('butterfly')
    return jsonify({"count": count, "decoder": decoder})

if __name__ == '__main__':
      # Expose to all external-facing IP addresses
      app.run(host='0.0.0.0', port=2526)