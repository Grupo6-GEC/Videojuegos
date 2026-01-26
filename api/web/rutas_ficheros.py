from __future__ import print_function
from flask import request,Blueprint, jsonify, send_from_directory
import controlador_ficheros
from funciones_token import token_existente
import os
import sys
import subprocess

bp = Blueprint('ficheros', __name__)

@bp.route ('/', methods=['POST']) 
def upload():

    auth = request.headers.get("Authorization")
    if not auth:
        return jsonify({"status": "ERROR", "message": "Token requerido"}), 401

    token = auth.replace("Bearer ", "")

    token_valido = token_existente({"token": token})

    if token_valido is False or token_valido["perfil"] != "admin":
        return jsonify({"status": "ERROR", "message": "No autorizado"}), 401


    try:
        contenido= request.files['fichero'] 
        nombre = request.form.get("nombre")
        respuesta,code = controlador_ficheros.guardar_fichero(nombre,contenido)
    except Exception as e:
        print(f"Error subiendo archivo: {e}", flush=True)
        respuesta={"status": "ERROR"}
        code=500
    return jsonify(respuesta), code

@bp.route ('/<archivo>', methods=['GET']) 
def ver(archivo):

    auth = request.headers.get("Authorization")
    if not auth:
        return jsonify({"status": "ERROR", "message": "Token requerido"}), 401

    token = auth.replace("Bearer ", "")
    token_valido = token_existente({"token": token})

    if token_valido is False:
        return jsonify({"status": "ERROR", "message": "Token inválido"}), 401

    basepath = os.path.dirname(__file__)
    ruta_fichero = os.path.join(basepath, 'static/archivos', archivo)
    try:
        contenido = subprocess.getoutput("cat " + ruta_fichero)
        return  jsonify({"contenido": contenido}), 200 #, {'Content-Type': 'text/plain; charset=utf-8'}
    except Exception as e:
        print(f"Error sirviendo archivo: {e}", flush=True)
        return "Archivo no encontrado", 404
