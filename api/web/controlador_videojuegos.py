from bd import obtener_conexion
import sys


def convertir_dbvideojuego_a_json(videojuego):
    d = {}
    d['id'] = videojuego[0]
    d['nombre'] = videojuego[1]
    d['foto'] = videojuego[2]
    d['descripcion'] = videojuego[3]
    d['precio'] = float(videojuego[4])
    d['creador'] = videojuego[5]
    d['ruta_foto']=videojuego[6]
    d['tienda']=videojuego[7]
    return d

###

def insertar_videojuego(nombre, foto, descripcion, precio, creador, ruta_foto, tienda):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO videojuegos(nombre, foto, descripcion, precio, creador, ruta_foto, tienda) VALUES (%s, %s, %s,%s,%s, %s, %s)",
                       (nombre, foto, descripcion, precio, creador, ruta_foto, tienda))
    conexion.commit()
    conexion.close()
    ret={"status": "OK" }
    code=200
    return ret,code

#####

def obtener_videojuegos():
    videojuegosjson=[]
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id, nombre, foto, descripcion, precio, creador, ruta_foto, tienda FROM videojuegos")
            videojuegos = cursor.fetchall()
            if videojuegos:
                for videojuego in videojuegos:
                    videojuegosjson.append(convertir_dbvideojuego_a_json(videojuego))
        conexion.close()
        code=200
    except:
        print("Error al consultar todos los videojuegos", flush=True)
        code=500
    return videojuegosjson,code

###

def obtener_videojuego_por_id(id):
    videojuegojson = {}
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id, nombre, foto, descripcion, precio, creador, ruta_foto, tienda FROM videojuegos WHERE id =" + id)
            videojuego = cursor.fetchone()
            if videojuego is not None:
                videojuegojson = convertir_dbvideojuego_a_json(videojuego)
        conexion.close()
        code=200
    except:
        print("Error al consultar un videojuego", flush=True)
        code=500
    return videojuegojson,code

###

def eliminar_videojuego(id):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM videojuegos WHERE id = %s", (id,))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret={"status": "Failure" }
        conexion.commit()
        conexion.close()
        code=200
    except:
        print("Error al eliminar un videojuego", flush=True)
        ret = {"status": "Failure" }
        code=500
    return ret,code

###

def actualizar_videojuego(id, nombre, foto, descripcion, precio, creador, ruta_foto, tienda):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE videojuegos SET nombre = %s, foto=%s, descripcion = %s, precio = %s, creador=%s, ruta_foto=%s, tienda=%s WHERE id = %s",
                       (nombre, foto, descripcion, precio, creador, ruta_foto, tienda, id))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret={"status": "Failure" }
        conexion.commit()
        conexion.close()
        code=200
    except:
        print("Error al actualizar un videojuego", flush=True)
        ret = {"status": "Failure" }
        code=500
    return ret,code
