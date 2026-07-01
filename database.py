# CONEXIÓN A LA BASE DE DATOS

import psycopg2

# Función para obtener la conexión a la base de datos
def get_conexion():
    try:
        conexion = psycopg2.connect(
            database='TareaPython',   
            user='postgres',          
            password='85271585r',       
            host='localhost',
            port='5432'
        )
        return conexion
    except psycopg2.Error as error:
        print("Error al conectar a la base de datos: ", error)
        return None


# Función para crear las tablas si no existen
def crear_tablas():
    conexion = get_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()

            ARRENDATARIO = """
            CREATE TABLE IF NOT EXISTS arrendatario (
                id_arrendatario INT PRIMARY KEY,
                nombre VARCHAR(100),
                ciudad VARCHAR(100),
                telefono VARCHAR(20)
            );
            """

            PROPIEDAD = """
            CREATE TABLE IF NOT EXISTS propiedad (
                id_propiedad INT PRIMARY KEY,
                direccion VARCHAR(150),
                tipo_propiedad VARCHAR(50),
                valor_mensual NUMERIC(10,2)
            );
            """

            ARRIENDO = """
            CREATE TABLE IF NOT EXISTS arriendo (
                id_arrendatario INT,
                id_propiedad INT,
                fecha_inicio DATE,
                fecha_termino DATE,
                monto_pagado NUMERIC(10,2),
                PRIMARY KEY (id_arrendatario, id_propiedad),
                FOREIGN KEY (id_arrendatario) REFERENCES arrendatario(id_arrendatario),
                FOREIGN KEY (id_propiedad) REFERENCES propiedad(id_propiedad)
            );
            """

            cursor.execute(ARRENDATARIO)
            cursor.execute(PROPIEDAD)
            cursor.execute(ARRIENDO)
            conexion.commit()
            print("Tablas creadas correctamente (o ya existían).")

        except psycopg2.Error as error:
            print("Error al crear las tablas: ", error)
        finally:
            cursor.close()
            conexion.close()


if __name__ == "__main__":
    crear_tablas()
