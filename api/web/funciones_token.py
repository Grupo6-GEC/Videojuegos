import jwt
import os
from datetime import datetime, timedelta, timezone
from controlador_token import Comprobar_token_invalidado

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

def token_existente(login_json):
    if not login_json or "token" not in login_json:
        return False
        #return {"error": "No se pudo obtener token","code":401}

    token = login_json["token"]
    token_decodificado = token_valido_no_baneado(token)
    if token_decodificado == False:
        return False
        #return {"status":"No autorizado","code":401}

    return  token_decodificado

def token_existente_rol_admin (login_json):
    if not login_json or "token" not in login_json:
        return {"error": "No se pudo obtener token"}, 500

    token = login_json["token"]

    valor_token = token_valido_no_baneado(token)

    if valor_token == False or valor_token["perfil"] != "admin":
        return {"status":"No autorizado"}, 401

    return True


def token_valido_no_baneado (token):

    token_decodificado = validar_token(token)

    if not token_decodificado:
        return False
        
    if not Comprobar_token_invalidado(token):
        return False

    return token_decodificado