from flask import request, Blueprint, jsonify
import controlador_videojuegos
from controlador_token import token_valido_no_baneado
from funciones_token import token_existente
from funciones_auxiliares import Encoder

bp = Blueprint('videojuego', __name__)

@bp.route("/",methods=["GET"])
def videojuegos():
    token_valido= token_existente(request.json)

    if token_valido == False:
        return jsonify({"status":"Token no valido"}), 401

    respuesta,code= controlador_videojuegos.obtener_videojuegos()
    return jsonify(respuesta), code

###

@bp.route("/<id>",methods=["GET"])
def videojuego_por_id(id):
    token_valido= token_existente(request.json)

    if token_valido == False:
        return jsonify({"status":"Token no valido"}), 401

    respuesta,code = controlador_videojuegos.obtener_videojuego_por_id(id)
    return jsonify(respuesta), code

###

@bp.route("/",methods=["POST"])
def guardar_videojuego():
    
    token_valido= token_existente(request.json)

    if token_valido == False or token_valido["perfil"] != "admin":
        return jsonify({"status":"Token no valido"}), 401
    
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        videojuego_json = request.json
        nombre = videojuego_json["nombre"]
        foto=videojuego_json["foto"]
        descripcion = videojuego_json["descripcion"]
        precio=videojuego_json["precio"]
        creador=videojuego_json["creador"]
        ruta_foto=videojuego_json["ruta_foto"]
        tienda=videojuego_json["tienda"]
        respuesta,code=controlador_videojuegos.insertar_videojuego(nombre, foto, descripcion, precio, creador, ruta_foto, tienda)
    else:
        respuesta={"status":"Bad request"}
        code=400
    return jsonify(respuesta), code

####

@bp.route("/<int:id>", methods=["DELETE"])
def eliminar_videojuego(id):

    token_valido= token_existente(request.json)

    if token_valido == False or token_valido["perfil"] != "admin":
        return jsonify({"status":"Token no valido"}), 401

    respuesta,code=controlador_videojuegos.eliminar_videojuego(id)
    return jsonify(respuesta), code

###

@bp.route("/", methods=["PUT"])
def actualizar_videojuego():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        videojuego_json = request.json
        id = videojuego_json["id"]
        nombre = videojuego_json["nombre"]
        foto=videojuego_json["foto"]
        descripcion = videojuego_json["descripcion"]
        try:
            precio=float(videojuego_json["precio"])
        except (ValueError, TypeError, KeyError):
            return jsonify({"status":"Precio invalido"}), 400
        creador=videojuego_json["creador"]
        ruta_foto=videojuego_json["ruta_foto"]
        tienda=videojuego_json["tienda"]
        respuesta,code=controlador_videojuegos.actualizar_videojuego(id, nombre, foto, descripcion, precio, creador, ruta_foto, tienda)
    else:
        respuesta={"status":"Bad request"}
        code=400
    return jsonify(respuesta), code

