import jwt
from datetime import datetime, timezone, timedelta
from config import SECRET_KEY

def generate_token(user_id):
    token = jwt.encode({
        'id': user_id,
        'exp': datetime.now(tz=timezone.utc)+timedelta(hours=3)
    }, SECRET_KEY, algorithm='HS256')
    
    return token

def check_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        print('Signature expired!')
        return False
    if payload:
        return payload
    else:
        return False