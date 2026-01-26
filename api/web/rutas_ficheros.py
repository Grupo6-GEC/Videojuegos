from __future__ import print_function
from flask import request,Blueprint, jsonify, send_from_directory
import controlador_ficheros
import os
import sys
import subprocess

bp = Blueprint('ficheros', __name__)

@bp.route ('/', methods=['POST']) 
def upload():
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
    basepath = os.path.dirname(__file__)
    ruta_fichero = os.path.join(basepath, 'static/archivos', archivo)
    try:
        contenido = subprocess.getoutput("cat " + ruta_fichero)
        return contenido, 200, {'Content-Type': 'text/plain; charset=utf-8'}
    except Exception as e:
        print(f"Error sirviendo archivo: {e}", flush=True)
        return "Archivo no encontrado", 404
