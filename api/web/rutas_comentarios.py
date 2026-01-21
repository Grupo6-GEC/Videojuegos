from __future__ import print_function
from flask import request,Blueprint, jsonify
import controlador_comentarios
from funciones_token import token_existente

bp = Blueprint('comentarios', __name__)

@bp.route("/",methods=['POST'])
def insertar_comentario():
    if request.headers.get('Content-Type') == 'application/json':
        data = request.json
        id_usuario = data['id_usuario']
        id_videojuego = data['id_videojuego']
        contenido = data['contenido']

        respuesta, code = controlador_comentarios.insertar_comentario(
            id_usuario, id_videojuego, contenido
        )
    else:
        respuesta = {"status": "Bad request"}
        code = 400

    return jsonify(respuesta), code

@bp.route("/",methods=['GET'])
def consulta_comentarios():

    token_valido= token_existente(request.json)

    if token_valido == False:
        return jsonify({"status":"Token no valido"}), 401

    respuesta, code = controlador_comentarios.obtener_comentarios()

    return jsonify(respuesta), code



