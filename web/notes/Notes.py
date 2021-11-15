from bson.objectid import ObjectId
from flask import jsonify, request
from flask_restful import Resource
from database.database import notes
from user.token import check_token


class Note(Resource):
  def post(self):
    # get posted data
    posted_data = request.get_json()
    try:
      date = posted_data['date']
      token = posted_data['token']
    except:
      return jsonify({'message': 'Error while getting posted data.'})

    # check token validity
    payload = check_token(token)
    if not payload:
      return jsonify({'message': 'Invalid token'})
    user_id = payload['id']

    # get the note from db
    cursor = notes.find({'date': date})
    if not cursor:
      return jsonify({'message': 'This note dont exist!'})

    # getting the note
    notes_dict = list(cursor)
    note_dict = {}
    for note in notes_dict:
      if note['user_id'] == user_id:
        note_dict = note
    note_dict['_id'] = str(note_dict['_id'])

    return note_dict

  def delete(self):
    # get posted data
    posted_data = request.get_json()
    try:
      note_id = posted_data['id']
      token = posted_data['token']
    except:
      return jsonify({'message': 'Error while getting posted data.'})

    # check token validity
    payload = check_token(token)
    if not payload:
      return jsonify({'message': 'Invalid token'})
    user_id = payload['id']

    # check note existance
    cursor = notes.find({'_id': note_id})
    if not cursor:
      return jsonify({'message': 'This note dont exist!'})

    # deleting the note
    try:
      notes.delete_one({'_id': ObjectId(note_id)})
    except:
      return jsonify({'message': 'Error while delete.'})

    # enviando mensagem de sucesso
    return jsonify({'message': 'Note deleted!'})


class Notes(Resource):
  def post(self):
    pass
