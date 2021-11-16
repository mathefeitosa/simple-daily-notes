import bcrypt
from flask import jsonify, request
from flask_restful import Resource
from database.database import users, generate_today_note

class Login(Resource):
  def post(self):
    # get posted data
    posted_data = request.get_json()

    # check if the parameters exits
    if 'email' not in posted_data or 'password' not in posted_data:
      return jsonify({'message': 'Incorrect parameters!'})

    # separating the data
    email = posted_data['email']
    password = posted_data['password']
    
    # getting user
    cursor = users.find({'email': email})
    
    # checking user existance
    if not cursor:
      return jsonify({'message': 'Unknown user!'})
    
    # getting the data from collections received
    user_dict = list(cursor)[0]
    user_id = str(user_dict['_id'])
    
    # checking if password match
    if not bcrypt.checkpw(password.encode(), user_dict['password']):
      return jsonify({'message': 'Incorrect password!'})
  
  
  
    # generating token
    from user.token import generate_token
    token = generate_token(user_id)
    
    # creating today note
    generate_today_note(user_id)
    
    # returning the token for future operations by the front-end
    return jsonify({'token':token})

