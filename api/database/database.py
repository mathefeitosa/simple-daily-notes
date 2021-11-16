from datetime import date, datetime
from flask import jsonify
from pymongo import MongoClient

client = MongoClient(
    'mongodb+srv://admin:admin@cluster0.uxp4g.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = client.dailyNotes
users = db['users']
notes = db['notes']

def today():
    day = datetime.today().date().day
    month = datetime.today().date().month
    year = datetime.today().date().year
    today = f'{month}/{day}/{year}'
    return today

def generate_today_note(user_id):
    # checks if the note already exists
    
    if notes.find_one({
        'date': today()
    }):
        return jsonify({'message': 'Today note already created.'})
    
    # insert the note
    notes.insert_one({
        'date': today(),
        'user_id': user_id,
        'text': ''
    })
