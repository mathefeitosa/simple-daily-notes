from flask import jsonify, request
from flask_restful import Resource
from bson.objectid import ObjectId
from database.database import users


class User(Resource):
  def post(self):
    # get posted data
    posted_data = request.get_json()

    # separating the data
    token = posted_data['token']

    # checking the token and getting payload
    from user.token import check_token
    payload = check_token(token)
    if not payload:
      return jsonify({'message': 'Token not valid!'})

    # getting payload data
    user_id = payload['id']

    print(user_id)
    # getting user
    data = users.find({'_id': ObjectId(user_id)}, {'password': 0})

    # checking user existance
    if not data:
      return jsonify({'message': 'This user dont exist! Where did you got this token?'})
    # getting user data and making a JSONizable
    user_dict = list(data)[0]
    user_dict['_id'] = str(user_dict['_id'])
    user_dict['token'] = token

    # getting the data from collections received
    return user_dict
