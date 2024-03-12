import jwt
import datetime





def encode_token(user):
    payload = {
        'id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow()
    }
    token = jwt.encode(payload, 'secret', algorithm='HS256')
    return token

def set_token_cookie(response, token):
    response.set_cookie(key='jwt', value=token, httponly=True)
    
def delete_token_cookie(response):
    response.delete_cookie('jwt')
    
def decode_token(token):
    return jwt.decode(token, 'secret', algorithms=['HS256'])