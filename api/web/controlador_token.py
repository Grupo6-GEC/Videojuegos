from bd import obtener_conexion
from datetime import datetime, timezone
import hashlib

#from funciones_token import validar_token


def insertar_token_invalido_db(token, token_decodificado):

    expiracion = token_decodificado["exp"]
    
    if isinstance(expiracion, int):
        expiracion = datetime.fromtimestamp(expiracion, tz=timezone.utc)

    if(expiracion<datetime.now(timezone.utc)):
        return {"status":"ERROR"},200

    token_hash = hashlib.sha256(token.encode('utf-8')).hexdigest()

    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT expiracion FROM lista_token_baneado WHERE token = %s",(token,))
            ya_baneado = cursor.fetchone()

            if ya_baneado is None:
                exp_str = expiracion.strftime('%Y-%m-%d %H:%M:%S')
                cursor.execute("INSERT INTO lista_token_baneado (token_hash,token,expiracion) VALUES  (%s,%s, %s)",(token_hash, token, exp_str))

                if cursor.rowcount == 1:
                    conexion.commit()
                    ret={"status": "Sesion cerrada con exito" }
                    code=200
                else:
                    ret={"status": "ERROR" }
                    code=500
            else:
                ret = {"status": "ERROR","mensaje": "Sesion ya cerrada"}
                code=200
        conexion.close()
    except Exception as e: 
        print("ERROR AL BANEAR TOKEN:", repr(e), flush=True)  
        ret={"status":"ERROR"}
        code=500
    return ret,code

def Comprobar_token_invalidado(token):

    token_hash = hashlib.sha256(token.encode('utf-8')).hexdigest()
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT count(*) FROM `lista_token_baneado` WHERE token_hash =%s",(token_hash,))
            baneado = cursor.fetchone()
        conexion.close()
        print(baneado)
        if baneado != 0:
            return True
        return False
    
    except Exception as e: 
        print("Fallo al comprobar token invalido:", repr(e), flush=True)  
        return False


def token_valido_no_baneado (token):
    return 0
#     token_decodificado = validar_token(token)

#     if not token_decodificado:
#         return False
        
#     if not Comprobar_token_invalidado(token):
#         return False

#     return token_decodificado

