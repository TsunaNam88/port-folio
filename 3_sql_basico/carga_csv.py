import pandas as pd
from sqlalchemy import create_engine

# import mysql.connector
import pymysql
import json
import sys


# Definir la función para leer las credenciales del archivo JSON
def read_keys(archivo_json: str) -> tuple:
    try:
        # Abrir y leer el archivo JSON
        with open(archivo_json, "r") as archivo:
            credenciales = json.load(archivo)
            # Extraer el usuario, password y host
            usuario = credenciales["usuario"]
            password = credenciales["password"]
            host = credenciales["host"]
            print(f"Credenciales leídas correctamente del archivo {archivo_json}")
            # Retornar los valores como una tupla
            return usuario, password, host
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo de configuración {archivo_json}")
        sys.exit()
    except KeyError:
        print(f"Error: El archivo {archivo_json} no tiene el formato esperado.")
        sys.exit()


# Definir la función para la conexión inicial a MySQL sin especificar la base de datos
def init_conn(usuario: str, password: str, host: str) -> tuple:
    try:
        # Crear la conexión a MySQL
        conexion_mysql = pymysql.connect(user=usuario, password=password, host=host)
        cursor = conexion_mysql.cursor()
        print(f"Conexión exitosa a MySQL en {host}")
        # Retornar la conexión y el cursor
        return conexion_mysql, cursor
    except pymysql.connect.Error as err:
        print(f"Error al conectar a MySQL: {err}")
        sys.exit()


# Crear la base de datos si no existe
def crear_base_sql(cursor, conexion_mysql, nombre_base_de_datos):
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {nombre_base_de_datos}")
        print(f"Base de datos '{nombre_base_de_datos}' verificada/creada.")
        cursor.close()
        conexion_mysql.close()
    except pymysql.connect.Error as err:
        print(f"Error al crear la base de datos: {err}")
        cursor.close()
        conexion_mysql.close()
        sys.exit()


def crear_tabla_sql(
    usuario: str,
    password: str,
    host: str,
    nombre_base_de_datos: str,
    tabla_mysql: str,
    archivo_csv: str,
):
    # Crear la conexión al motor de MySQL con la base de datos especificada
    motor = create_engine(
        f"mysql+mysqlconnector://{usuario}:{password}@{host}/{nombre_base_de_datos}"
    )
    # Leer el CSV usando pandas
    try:
        datos_csv = pd.read_csv(
            archivo_csv,
            sep=",",
            on_bad_lines="skip",
            parse_dates=["entry_date", "last_update"],
        )
        datos_csv["entry_date"] = pd.to_datetime(
            datos_csv["entry_date"], format="ISO8601"
        )
        datos_csv["last_update"] = pd.to_datetime(
            datos_csv["last_update"], format="ISO8601"
        )
        print(f"Datos leídos correctamente del archivo CSV: {archivo_csv}")
    except FileNotFoundError:
        print(f"Error: El archivo CSV no se encuentra en la ruta: {archivo_csv}")
        sys.exit()
    # Insertar datos en la tabla MySQL
    try:
        datos_csv.to_sql(tabla_mysql, con=motor, if_exists="replace", index=False)
        print(f"Datos insertados correctamente en la tabla '{tabla_mysql}' de MySQL.")
    except Exception as e:
        print(f"Error al insertar los datos en MySQL: {str(e)}")


if __name__ == "__main__":
    # Ruta del archivo JSON con las credenciales
    archivo_json = "C:\\Users\\tsuda\\dataelite\\dataelite2024\\04_SQL_basico\\Retos\\Soluciones\\claves.json"
    usuario, password, host = read_keys(archivo_json)
    # Variables de conexión MySQL
    nombre_base_de_datos = "sale_data"
    conexion_mysql, cursor = init_conn(usuario, password, host)
    crear_base_sql(cursor, conexion_mysql, nombre_base_de_datos)
    # Nombre de la tabla MySQL
    tabla_mysql = "test_data_date2"
    # Ruta del archivo CSV
    archivo_csv = "04_SQL_basico/data_glucosa/data_publicaciones.csv"
    crear_tabla_sql(
        usuario, password, host, nombre_base_de_datos, tabla_mysql, archivo_csv
    )
# source env_pruebas/bin/activate
# 1369
