from __future__ import print_function
from flask import request,Blueprint, jsonify
import controlador_comentarios
from funciones_token import token_existente

bp = Blueprint('comentarios', __name__)
@bp.route("/", methods=['POST'])

def insertar_comentario():

    # 1. Leer token del HEADER
    auth = request.headers.get("Authorization")
    if not auth:
        return jsonify({"status": "ERROR", "message": "Token requerido"}), 401

    token = auth.replace("Bearer ", "")

    # 2. Validar token
    token_valido = token_existente({"token": token})
    if token_valido is False:
        return jsonify({"status": "ERROR", "message": "No autorizado"}), 401

    # 3. Leer datos
    data = request.json
    if not data or not all(k in data for k in ("id_videojuego", "contenido")):
        return jsonify({"status": "ERROR", "message": "Datos incompletos"}), 400

    if not data["contenido"].strip():
        return jsonify({"status": "ERROR", "message": "Contenido vacío"}), 400

    # 4. ID DEL USUARIO DESDE EL TOKEN
    id_usuario = token_valido["id"]

    # 5. Insertar comentario
    respuesta, code = controlador_comentarios.insertar_comentario(
        id_usuario,
        data["id_videojuego"],
        data["contenido"]
    )

    return jsonify(respuesta), code

@bp.route("/", methods=['GET'])
def consulta_comentarios():

    auth = request.headers.get("Authorization")
    if not auth:
        return jsonify({"status": "ERROR", "message": "Token requerido"}), 401

    token = auth.replace("Bearer ", "")
    token_valido = token_existente({"token": token})

    if token_valido is False:
        return jsonify({"status": "ERROR", "message": "Token inválido"}), 401

    respuesta, code = controlador_comentarios.obtener_comentarios()
    return jsonify(respuesta), code




