#!/usr/bin/env python
import io
from pathlib import Path
from random import randrange, random, choice
from time import sleep
from flask import Flask, make_response, redirect, request, Response, stream_with_context
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()
greetings = Path('greetings.txt').read_text().splitlines()

@app.route('/data')
def data():
    lines = io.StringIO()
    for _ in range(randrange(10, 20)):
        greet = choice(greetings)
        num = randrange(1, 1000)
        val = random()
        print(f'{greet},{num},{val*100}', file=lines)
    csv = "GREETING,NUMBER,VALUE\n" + lines.getvalue()
    resp = make_response(csv)
    resp.mimetype = 'text/csv'
    resp.headers['X-INE-Course'] = "HTTP using Python"
    return resp


@app.route('/redirect')
def to_kdm():
    return redirect("http://kdm.training", code=301)


@app.route('/add', methods=["PUT", "POST"])
def sum_csv():
    csv = request.get_data().decode()
    total = sum(float(l.split(',')[2]) for l in csv.splitlines()[1:])
    resp = make_response(str(total))
    resp.mimetype = 'text/plain'
    return resp


@app.route('/form', methods=["PUT", "POST"])
def form():
    html = f"""
      <html>
        <head>
          <title>INE Student Summary</title>
        </head>
        <body>
          <h3>HTTP using Python</h3>
          <dl>
            <dt>Name</dt><dd>{request.form['name']}</dd>
            <dt>Favorite Color</dt><dd>{request.form['color']}</dd>
            <dt>Birthday</dt><dd>{request.form['bday']}</dd>
          </dl>
        </body>
      </html>
    """
    return make_response(html)


@app.route('/stream')
def streamed_response():
    def generate():
        for _ in range(10):
            greet = choice(greetings)
            yield greet
            yield '\n'
            sleep(random()*3)
    return Response(generate(), mimetype='text/plain')            

users = {
    "David": generate_password_hash("4bYaDZCFsTY4"),
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@app.route('/secure')
@auth.login_required
def secure():
    return f"Hello, {auth.current_user()}!"


if __name__ == '__main__':
    # Expose to all external-facing IP addresses
    from werkzeug.serving import WSGIRequestHandler
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run(host='0.0.0.0', port=2502)

