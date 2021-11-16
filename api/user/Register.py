import bcrypt
from flask import jsonify, request
from flask_restful import Resource

from database.database import users

def generate_hash_password(password):
  # generating password -> hash(password+salt)
  return bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())


class Register(Resource):
  def post(self):
    # get posted data
    posted_data = request.get_json()

    # check if the parameters exits
    if 'email' not in posted_data or 'password' not in posted_data:
      return jsonify({'message': 'Incorrect parameters!'})

    # separating the data
    email = posted_data['email']
    password = posted_data['password']

    # check if the user already exists
    if users.find_one({'email': email}):
        return jsonify({'message': 'This user already exists!'})
    
    # store username and hash in the database
    response = users.insert_one({
        "email": email,
        'password': generate_hash_password(password),
    })
    user_id = str(response.inserted_id)
    
    # generating JWT
    from user.token import generate_token
    token = generate_token(user_id)
    
    return jsonify({
        'token': token,
    })
