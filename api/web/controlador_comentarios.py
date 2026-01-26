from bd import obtener_conexion


def convertir_comentario_a_json(comentario):
    d = {}
    d['id'] = comentario[0]
    d['usuario'] = comentario[1]
    d['videojuego'] = comentario[2]
    d['contenido'] = comentario[3]
    return d

def obtener_usuario_por_nombre(username):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id FROM usuarios WHERE usuario = %s", (username,))
            result = cursor.fetchone()
        conexion.close()
        return result[0] if result else None
    except Exception as e:
        print("Error al buscar usuario:", e, flush=True)
        return None

def insertar_comentario(username, id_videojuego, contenido):
    try:
        id_usuario = obtener_usuario_por_nombre(username)
        if id_usuario is None:
            return {"status": "ERROR", "mensaje": "Usuario no encontrado"}, 404

        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            sql = """
                INSERT INTO comentarios (id_usuario, id_videojuego, contenido)
                VALUES (%s, %s, %s)
            """
            cursor.execute(sql, (id_usuario, id_videojuego, contenido))
            conexion.commit()
        conexion.close()
        return {"status": "OK"}, 200
    except Exception as e:
        print("Error al insertar comentario:", e, flush=True)
        return {"status": "ERROR", "mensaje": str(e)}, 500


def obtener_comentarios():
    comentariosjson = []
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            sql = """
                SELECT c.id, u.usuario, v.nombre, c.contenido
                FROM comentarios c
                JOIN usuarios u ON c.id_usuario = u.id
                JOIN videojuegos v ON c.id_videojuego = v.id
            """
            cursor.execute(sql)
            comentarios = cursor.fetchall()
            for comentario in comentarios:
                comentariosjson.append(convertir_comentario_a_json(comentario))
        conexion.close()
        return comentariosjson, 200
    except Exception as e:
        print("Error al obtener comentarios:", e, flush=True)
        return [], 500