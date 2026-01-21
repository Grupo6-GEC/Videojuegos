from bd import obtener_conexion
import sys
import datetime as dt
from funciones_token import generar_token

def login_usuario(username,password):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT perfil FROM usuarios WHERE usuario = %s and clave= %s",(username,password))
            usuario = cursor.fetchone()
            
            if usuario is None:
                ret = {"status": "ERROR","mensaje":"Usuario/clave erroneo" }
            else:
                perfil = usuario[0]
                token = generar_token(username,perfil)
                print("TOKEN:", token, flush=True)
                ret = {"status": "OK","token": token}
        code=200
        conexion.close()
    except:
        print("Excepcion al validar al usuario", flush=True) 
        print("ERROR REAL:", repr(e), flush=True)  
        ret={"status":"ERROR"}
        code=500
    return ret,code

def alta_usuario(username,password,perfil):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT perfil FROM usuarios WHERE usuario = %s",(username,))
            usuario = cursor.fetchone()
            if usuario is None:

                cursor.execute("INSERT INTO usuarios(usuario,clave) VALUES(%s,%s)",(username,password))

                if cursor.rowcount == 1:
                    conexion.commit()
                    ret={"status": "OK" }
                    code=200
                else:
                    ret={"status": "ERROR" }
                    code=500
            else:
                ret = {"status": "ERROR","mensaje":"Usuario ya existe" }
                code=200
        conexion.close()
    except:
        print("Excepcion al registrar al usuario", flush=True)   
        ret={"status":"ERROR"}
        code=500
    return ret,code    


