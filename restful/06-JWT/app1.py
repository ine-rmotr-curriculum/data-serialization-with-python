#!/usr/bin/env python
from flask import Flask
app = Flask(__name__)

data = {'Admin': {
            'Alice': {
                'Carlos': None,
                'David': {
                    'Eunice': None,
                    'Frances': None
                }
            },
            'Bob': {
                
            }}
       }


# route for loging user in
@app.route('/login', methods =['POST'])
def login():
    cred = request.form
   
    if not cred.get('username') or not cred.get('password'):
        # returns 401 if any email or / and password is missing
        return make_response('Could not verify', 401,
            {'WWW-Authenticate' : 'Basic realm ="Login required !!"'})
   
    if not cred.get('username'):
        # returns 401 if user does not exist
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate' : 'Basic realm ="User does not exist !!"'}
        )
   
    if check_password_hash(user.password, auth.get('password')):
        # generates the JWT Token
        token = jwt.encode({
            'public_id': user.public_id,
            'exp' : datetime.utcnow() + timedelta(minutes = 30)
        }, app.config['SECRET_KEY'])
   
        return make_response(jsonify({'token' : token.decode('UTF-8')}), 201)
    # returns 403 if password is wrong
    return make_response(
        'Could not verify',
        403,
        {'WWW-Authenticate' : 'Basic realm ="Wrong Password !!"'}
    )


if __name__ == "__main__":
    app.run(ssl_context=('pubkey.pem', 'private.pem'), port=5001)