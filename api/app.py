
from notes.Notes import TodayNote, AllMyNotes, Note
from flask import Flask
from flask_restful import Api
from user.Register import Register
from user.Login import Login
from user.User import User

# starting the flask app and running restful API module
app = Flask(__name__)
api = Api(app)


# routes
api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
api.add_resource(User, '/user')
api.add_resource(TodayNote, '/notes/today')
api.add_resource(AllMyNotes, '/notes')
api.add_resource(Note, '/note')


if __name__ == '__main__':
  app.run(host='0.0.0.0')
