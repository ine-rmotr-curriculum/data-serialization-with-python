#!/usr/bin/env python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Secret Message!"

# route for loging user in
@app.route('/login', methods =['POST'])
def login():
    # creates dictionary of form data
    auth = request.form
   
    if not auth or not auth.get('email') or not auth.get('password'):
        # returns 401 if any email or / and password is missing
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate' : 'Basic realm ="Login required !!"'}
        )
   
    user = User.query\
        .filter_by(email = auth.get('email'))\
        .first()
   
    if not user:
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