from flask_restful import Resource


class Homepage(Resource):
  def get(self):
    return 'This API is running!', 200
