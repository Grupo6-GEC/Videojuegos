from __future__ import print_function
from flask import request,Blueprint, jsonify
import controlador_comentarios

bp = Blueprint('comentarios', __name__)

@bp.route("/",methods=['POST'])
def insertar_comentario():
    if request.headers.get('Content-Type') == 'application/json':
        data = request.json
        username = data.get('username')
        id_videojuego = data.get('id_videojuego')
        contenido = data.get('contenido')

        if not username or not id_videojuego or not contenido:
            return jsonify({"status": "ERROR", "mensaje": "Faltan datos"}), 400

        respuesta, code = controlador_comentarios.insertar_comentario(
            username, id_videojuego, contenido
        )
    else:
        respuesta = {"status": "Bad request"}
        code = 400

    return jsonify(respuesta), code

@bp.route("/",methods=['GET'])
def consulta_comentarios():
    respuesta, code = controlador_comentarios.obtener_comentarios()
    return jsonify(respuesta), code



