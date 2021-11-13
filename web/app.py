from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt
import json
import hashlib
import base64
import hmac

SECRET_KEY = 'fqj4mnp9832kmpormgpjsdfngkldflkjrgnpqiowupur483048934t89q4j13r'

app = Flask(__name__)
api = Api(app)

client = MongoClient('mongodb://db:27017')
db = client.dailyNotes
users = db['users']


class Register(Resource):
  def post(self):
    posted_data = request.get_json()

    # get posted data
    posted_data = request.get_json()

    # check if the parameters exits
    if 'email' not in posted_data or 'password' not in posted_data:
      return jsonify({'message': 'Incorrect parameters!'})

    # getting the data
    email = posted_data['email']
    password = posted_data['password']

    # generating password -> hash(password+salt)
    hashed_password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

    # store username and hash in the database
    user = users.insert_one({
        "email": email,
        'password': hashed_password,
    })

    # generating user token
    header = json.dumps({
        'typ': 'JWT',
        'alg': 'HS256'
    }).encode()
    payload = {
        'userId': user.id,
        'exp': 1556841600
    }
    b64_header = base64.urlsafe_b64encode(header).decode()
    b64_payload = base64.urlsafe_b64encode(payload).decode()
    signature = hmac.new(
        key=SECRET_KEY.encode(),
        msg=f'{b64_header}.{b64_payload}'.encode(),
        digestmod=hashlib.sha256()
    ).digest()
    JWT = f'{b64_header}.{b64_payload}.{base64.urlsafe_b64encode(signature).decode()}'
    user.token = JWT

    # returning the status
    return jsonify(user)


api.add_resource(Register, '/register')

if __name__ == '__main__':
  app.run(debug=True)
