from flask import Flask, make_response, request, send_file, abort, jsonify
app = Flask(__name__)

@app.route('/')
def root():
    page = """<html>
    <head>
        <title>Test Server #1</title>
    </head>
    <body>
    <table>
        <tr><th>Path</th><th>Parameters</th></tr>
        <tr><td>/text</td><td>N/A</td></tr>
        <tr><td>/image</td><td>JPEG filename</td></tr>
        <tr><td>/json</td><td>Echo all</td></tr>
    </table>
    </body>
    </html>
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
    fname = f"{request.args.get('name', '1')}.jpg"
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
    


