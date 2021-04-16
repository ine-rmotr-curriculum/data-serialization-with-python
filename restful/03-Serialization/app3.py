#!/usr/bin/env python
import numpy as np
import pickle, io
from flask import Flask, request, abort, make_response
app = Flask(__name__)

@app.route('/add100', methods=["POST"])
def add100():
    if (request.content_type == 'application/octet-stream' 
            and request.headers['X-INE-type'] == "pickle"):
        arr = pickle.loads(request.data)
        arr += 100
        resp = make_response(pickle.dumps(arr))
        resp.mimetype = 'application/octet-stream'
        resp.headers['X-INE-type'] = "pickle"
        return resp
    elif request.content_type == 'application/vnd.ine.numpy':
        print(request.data[:80])
        arr = np.load(io.BytesIO(request.data))
        arr += 100
        buffer = io.BytesIO()
        np.save(buffer, arr)
        resp = make_response(buffer.getvalue())
        resp.mimetype = 'application/vnd.ine.numpy'
        return resp        
    else:
        abort(400)  # 400 Bad Request

if __name__ == '__main__':
      # Expose to all external-facing IP addresses
      app.run(host='0.0.0.0', port=2527)