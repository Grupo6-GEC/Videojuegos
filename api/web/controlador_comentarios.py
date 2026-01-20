from bd import obtener_conexion


def convertir_comentario_a_json(comentario):
    d = {}
    d['id'] = comentario[0]
    d['usuario'] = comentario[1]
    d['videojuego'] = comentario[2]
    d['contenido'] = comentario[3]
    return d

def insertar_comentario(id_usuario, id_videojuego, contenido):
    try:
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
        return {"status": "ERROR"}, 500

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