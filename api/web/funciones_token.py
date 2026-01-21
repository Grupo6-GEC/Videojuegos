import jwt
import os
from datetime import datetime, timedelta, timezone

tiempoDeSesion = 30


#def decodificar_token (token):
#    return jwt.decode(token, os.environ.get("TOKEN_SECRET"), algorithms=os.environ.get("ALGORITMO"))

def generar_token (username,perfil):
    ahora = datetime.now(timezone.utc)
    expira = ahora + timedelta(minutes=tiempoDeSesion)
    datos = {
        "username": username,
        "perfil": perfil,
        "exp": int(expira.timestamp())
    }
    return jwt.encode(datos, os.environ.get("TOKEN_SECRET"), algorithm=os.environ.get("ALGORITMO"))

def validar_token (token):
    try:
        decoded = jwt.decode(token, os.environ.get("TOKEN_SECRET"), algorithms=os.environ.get("ALGORITMO"))
        return decoded
    except jwt.ExpiredSignatureError:
        print ("Token expirado: "+ token)
        return False
    except jwt.InvalidTokenError:
        print ("Token invalido: "+ token)
        return False

