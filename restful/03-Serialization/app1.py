#!/usr/bin/env python
from flask import Flask, request, send_file, jsonify, abort, make_response
app = Flask(__name__)

@app.route('/')
def root():
    page = """<html><body><table>
        <tr><th>Path</th><th>Parameters</th></tr>
        <tr><td>/text</td><td>N/A</td></tr>
        <tr><td>/image</td><td>JPEG filename</td></tr>
        <tr><td>/json</td><td>Echo all</td></tr>
    </table></body></html>
    """
    r = make_response(page)
    r.mimetype = 'text/html'
    r.headers['X-INE-Course'] = "RESTful APIs"
    return r

@app.route('/text')
def text():
    r = make_response("Hello student!")
    r.mimetype = 'text/plain'
    return r

@app.route('/image')
def image():
    default = 'rainbow-butterfly-unicorn-kitten'
    fname = f"{request.args.get('name', default)}.jpg"
    try:
        return send_file(fname, mimetype='image/jpeg')
    except:
        abort(404)
        
@app.route('/json', methods=["GET", "POST", "PUT"])
def json():
    if request.method in {"PUT", "POST"}: 
        resp = dict(request.form)
    else:
        resp = dict(request.args)
    resp['Server'] = "Test Server #1"
    return jsonify(resp)

if __name__ == '__main__':
      # Expose to all external-facing IP addresses
      app.run(host='0.0.0.0', port=2525)