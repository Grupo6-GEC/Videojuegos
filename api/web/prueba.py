from flask import request,Blueprint, jsonify
from funciones_token import token_valido_no_baneado


bp = Blueprint('usuarios', __name__)

@bp.route("/prueba",methods=['POST'])
def prueba():
    login_json = request.json
    token = login_json["token"]
    respuesta = token_valido_no_baneado(token)
    return jsonify(respuesta), 200