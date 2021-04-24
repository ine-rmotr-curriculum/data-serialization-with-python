from time import time
from random import shuffle, random
from flask import Flask, make_response, request, send_file, abort, jsonify
app = Flask(__name__)

nasa_files = [
    ("image/jpeg", "NASA-mars.jpg", 
                 "Composite picture of Mars"),
    ("audio/wav", "Sol16RoverDriveHighlights.wav", 
                 "Audio recording of Mars"),
    ("application/pdf", "hubblefocusgalaxies.pdf", 
                 "PDF Document on Hubble telescope"),
    ("text/html", "NASA.html", 
                 "Article on Mars oxygen extraction")
]

last_access = time()

@app.route('/NASA')
def NASA():
    shuffle(nasa_files)
    mimetype, fname, desc = nasa_files[0]
    resp = make_response(send_file(fname, mimetype=mimetype))
    resp.headers['X-Description'] = desc
    return resp

@app.route('/Slow-NASA')
def Slow_NASA():
    global last_access
    now, old_last_access = time(), last_access
    last_access = now
    
    if now - old_last_access < 4 + random()*2.5:
        abort(503)

    shuffle(nasa_files)
    mimetype, fname, desc = nasa_files[0]
    resp = make_response(send_file(fname, mimetype=mimetype))
    resp.headers['X-Description'] = desc
    return resp

    


