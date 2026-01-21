from __future__ import print_function
from flask import request,Blueprint, jsonify
import controlador_comentarios
from funciones_token import token_existente

bp = Blueprint('comentarios', __name__)

@bp.route("/",methods=['POST'])
def login():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        comentario_json = request.json
        usuario = comentario_json['usuario']
        descripcion = comentario_json['descripcion']
        respuesta,code= controlador_comentarios.insertar_comentario(usuario,descripcion)
    else:
        respuesta={"status":"Bad request"}
        code=401
    return jsonify(respuesta), code

@bp.route("/",methods=['GET'])
def consulta_comentarios():

    token_valido= token_existente(request.json)

    if token_valido == False:
        return jsonify({"status":"Token no valido"}), 401

    respuesta, code = controlador_comentarios.obtener_comentarios()

    return jsonify(respuesta), code



