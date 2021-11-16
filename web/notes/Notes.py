from bson.objectid import ObjectId
from flask import jsonify, request
from flask_restful import Resource
from database.database import notes, today
from user.token import check_token

class Note(Resource):
  
  def post(self):
    # get posted data
    posted_data = request.get_json()
    try:
      token = posted_data['token']
      date = posted_data['date']
    except:
      return jsonify({'message': 'Error while getting posted data.'})

    # check token validity
    payload = check_token(token)
    if not payload:
      return jsonify({'message': 'Invalid token'})
    user_id = payload['id']
    
    # check note existance
    doc = notes.find_one({'user_id': user_id, 'date': date})
    if not doc:
      # creating new note
      try:
        notes.insert_one({'date': date, 'user_id': user_id, 'text': ''})
        
        # enviando mensagem de sucesso
        return jsonify({'message': 'Note created!'})
      except:
        return jsonify({'message': 'Error while creating the note.'})
    else:
      return jsonify({'message': 'This note already exists!'})
    

    
    
  # delete note by id
  def delete(self):
    # get posted data
    posted_data = request.get_json()
    try:
      note_id = posted_data['id']
      token = posted_data['token']
    except:
      return jsonify({'message': 'Error while getting posted data.'})

    # check token validity
    if not check_token(token):
      return jsonify({'message': 'Invalid token'})

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

  # update note by id
  def patch(self):
    # get posted data
    posted_data = request.get_json()
    try:
      note_id = posted_data['id']
      token = posted_data['token']
      text = posted_data['text']
    except:
      return jsonify({'message': 'Error while getting posted data.'})

    # check token validity
    if not check_token(token):
      return jsonify({'message': 'Invalid token'})

    # check note existance
    cursor = notes.find({'_id': note_id})
    if not cursor:
      return jsonify({'message': 'This note dont exist!'})

    # updating the note
    try:
      notes.find_one_and_update({'_id': ObjectId(note_id)}, {'$set': {'text':text}})
    except:
      return jsonify({'message': 'Error while updating the note.'})

    # enviando mensagem de sucesso
    return jsonify({'message': 'Note updated!'})

class AllMyNotes(Resource):
  # get all notes from a user
  def post(self):
    # get posted data
    posted_data = request.get_json()
    try:
      token = posted_data['token']
    except:
      return jsonify({'message': 'Error while getting posted data.'})

    # check token validity
    payload = check_token(token)
    if not payload:
      return jsonify({'message': 'Invalid token'})
    user_id = payload['id']

    # get the note from db
    cursor = notes.find({'user_id': user_id})
    if not cursor:
      return jsonify({'message': 'This user dont have notes!'})

    # getting the note
    notes_dict = list(cursor)
    note_list = []
    for note in notes_dict:
      if note['user_id'] == user_id:
        n = note
        n['_id'] = str(n['_id'])
        note_list.append(n)
    return note_list

class TodayNote(Resource):
  def post(self):
    # get posted data
    posted_data = request.get_json()
    try:
      token = posted_data['token']
    except:
      return jsonify({'message': 'Error while getting posted data.'})

    # check token validity
    payload = check_token(token)
    if not payload:
      return jsonify({'message': 'Invalid token'})
    user_id = payload['id']

    # get the note from db
    cursor = notes.find({'date': today()})
    if not cursor:
      return jsonify({'message': 'This note dont exist!'})

    # getting the note
    notes_dict = list(cursor)
    note_dict = {}
    for note in notes_dict:
      if note['user_id'] == user_id:
        note_dict = note
    note_dict['_id'] = str(note_dict['_id'])

    # returning the data
    return note_dict
  

  
    
