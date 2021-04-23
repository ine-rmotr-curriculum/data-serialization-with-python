#!/usr/bin/env python
from flask import Flask, abort, make_response, request
app = Flask(__name__)

# route for loging user in
@app.route('/getkey')
def getkey():
    service = request.args.get('identity')
    if not service:
        abort(403)
    else:
        try:
            key = open(f"{service}.key.pub").read()
            resp = make_response(key)
            resp.mimetype = 'application/X-rsa-public-key'
            return resp
        except Exception as err:
            # Probably not an available server name
            return make_response(str(err), 404)

if __name__ == "__main__":
    app.run(port=5010)