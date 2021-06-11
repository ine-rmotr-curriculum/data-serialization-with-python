#!/usr/bin/env python
from time import sleep
from flask import Flask, request, make_response, Response, stream_with_context
app = Flask(__name__)

@app.route('/greeting')
def greeting():
    lang = request.args.get('lang', 'en')
    greet = {'en': 'Hello', 'zh': 'Nǐn hǎo', 'fr': 'Bonjour'}[lang]
    who = request.headers.get('X-INE-Student', 'Student')
    page = f"""
      <html>
        <head>
          <title>Test Page</title>
        </head>
        <body>
          <p>{greet} {who}!</p>
        </body>
      </html>
    """
    resp = make_response(page)
    resp.mimetype = 'text/html'
    resp.headers['X-INE-Course'] = "HTTP using Python"
    return resp


@app.route('/stream')
def streamed_response():
    def generate():
        sleep(2)
        for greet in ('Hello', 'Nǐn hǎo', 'Bonjour', 'Hola', 'Zdravstvuyte'):
            yield greet
            sleep(4)
        yield '⌁'
    return app.response_class(stream_with_context(generate()))

if __name__ == '__main__':
    # Expose to all external-facing IP addresses
    from werkzeug.serving import WSGIRequestHandler
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run(host='0.0.0.0', port=2501)

