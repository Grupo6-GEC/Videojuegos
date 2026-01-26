import os
import pymysql

def obtener_conexion():
    required_vars = ['DB_HOST', 'DB_USERNAME', 'DB_PASSWORD', 'DB_DATABASE']
    for var in required_vars:
        if os.environ.get(var) is None:
            raise ValueError(f"Variable de entorno {var} no definida")
    return pymysql.connect(host=os.environ.get('DB_HOST'),
                                user=os.environ.get('DB_USERNAME'),
                                password=os.environ.get('DB_PASSWORD'),
                                port=int(os.environ.get('DB_PORT', 3306)),
                                db=os.environ.get('DB_DATABASE'))