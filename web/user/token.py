import jwt

from config import SECRET_KEY

def generate_token(user_id):
    token = jwt.encode({
        'id': user_id,
    }, SECRET_KEY, algorithm='HS256')
    
    return token

def check_token(token):
    payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    if payload:
        return payload
    else:
        return False