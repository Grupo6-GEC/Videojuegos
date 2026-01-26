from __future__ import print_function
from flask import request,Blueprint, jsonify
from funciones_auxiliares import Encoder
import controlador_usuarios
from controlador_token import insertar_token_invalido_db, token_valido_no_baneado
from funciones_token import token_existente

bp = Blueprint('usuarios', __name__)

@bp.route("/login",methods=['POST'])
def login():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        login_json = request.json
        username = login_json['username']
        password = login_json['password']
        respuesta,code= controlador_usuarios.login_usuario(username,password)
    else:
        respuesta={"status":"Bad request"}
        code=401
    return jsonify(respuesta), code

@bp.route("/registro",methods=['POST'])
def registro():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        login_json = request.json
        username = login_json['username']
        password = login_json['password']
        #profile = login_json['profile']
        respuesta,code= controlador_usuarios.alta_usuario(username,password)
    else:
        respuesta={"status":"Bad request"}
        code=401
    return jsonify(respuesta), code

@bp.route("/logout",methods=['POST'])
def logout():

    auth = request.headers.get("Authorization")
    if not auth:
        return jsonify({"status": "ERROR", "message": "Token requerido"}), 401

    token = auth.replace("Bearer ", "")

    token_valido = token_existente({"token": token})
    if token_valido is False:
        return jsonify({"status": "ERROR", "message": "No autorizado"}), 401


    respuesta,code= insertar_token_invalido_db(token, token_valido)
    return jsonify(respuesta), code

#recordar añadir token_valido_no_baneado a controlador_token
@bp.route("/prueba",methods=['POST'])
def prueba():
    if not request.is_json:
        return jsonify({"status":"Bad request"}), 400
    login_json = request.json
    if "token" not in login_json:
        return jsonify({"status":"Missing token"}), 400
    token = login_json["token"]
    
    respuesta = token_valido_no_baneado(token)
    return jsonify(respuesta), 200

