# ARCHIVO PARA REALIZAR OPERACIONES CRUD EN LA BASE DE DATOS

from database import get_conexion


# ---------------------------------------------------------
# CRUD ARRENDATARIO
# ---------------------------------------------------------

def insertar_arrendatario(id_arrendatario, nombre, ciudad, telefono):
    conexion = get_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = """INSERT INTO arrendatario (id_arrendatario, nombre, ciudad, telefono)
                    VALUES (%s, %s, %s, %s)"""
            cursor.execute(query, (id_arrendatario, nombre, ciudad, telefono))
            conexion.commit()
            print("Arrendatario agregado exitosamente.")
        except Exception as e:
            print("Error al insertar arrendatario: ", e)
        finally:
            cursor.close()
            conexion.close()


def consultar_arrendatarios():
    conexion = get_conexion()
    resultado = []
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM arrendatario;")
            resultado = cursor.fetchall()
        except Exception as e:
            print("Error al consultar arrendatarios: ", e)
        finally:
            cursor.close()
            conexion.close()
    return resultado


def actualizar_arrendatario(id_arrendatario, nombre, ciudad, telefono):
    conexion = get_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = """UPDATE arrendatario
                    SET nombre = %s, ciudad = %s, telefono = %s
                    WHERE id_arrendatario = %s"""
            cursor.execute(query, (nombre, ciudad, telefono, id_arrendatario))
            conexion.commit()
            print("Arrendatario actualizado exitosamente.")
        except Exception as e:
            print("Error al actualizar arrendatario: ", e)
        finally:
            cursor.close()
            conexion.close()


# CRUD PROPIEDAD


def insertar_propiedad(id_propiedad, direccion, tipo_propiedad, valor_mensual):
    conexion = get_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = """INSERT INTO propiedad (id_propiedad, direccion, tipo_propiedad, valor_mensual)
                    VALUES (%s, %s, %s, %s)"""
            cursor.execute(query, (id_propiedad, direccion, tipo_propiedad, valor_mensual))
            conexion.commit()
            print("Propiedad agregada exitosamente.")
        except Exception as e:
            print("Error al insertar propiedad: ", e)
        finally:
            cursor.close()
            conexion.close()


def consultar_propiedades():
    conexion = get_conexion()
    resultado = []
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM propiedad;")
            resultado = cursor.fetchall()
        except Exception as e:
            print("Error al consultar propiedades: ", e)
        finally:
            cursor.close()
            conexion.close()
    return resultado


def actualizar_propiedad(id_propiedad, direccion, tipo_propiedad, valor_mensual):
    conexion = get_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = """UPDATE propiedad
                    SET direccion = %s, tipo_propiedad = %s, valor_mensual = %s
                    WHERE id_propiedad = %s"""
            cursor.execute(query, (direccion, tipo_propiedad, valor_mensual, id_propiedad))
            conexion.commit()
            print("Propiedad actualizada exitosamente.")
        except Exception as e:
            print("Error al actualizar propiedad: ", e)
        finally:
            cursor.close()
            conexion.close()


# ---------------------------------------------------------
# CRUD ARRIENDO
# ---------------------------------------------------------

def insertar_arriendo(id_arrendatario, id_propiedad, fecha_inicio, fecha_termino, monto_pagado):
    conexion = get_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = """INSERT INTO arriendo (id_arrendatario, id_propiedad, fecha_inicio, fecha_termino, monto_pagado)
                    VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(query, (id_arrendatario, id_propiedad, fecha_inicio, fecha_termino, monto_pagado))
            conexion.commit()
            print("Arriendo agregado exitosamente.")
        except Exception as e:
            print("Error al insertar arriendo: ", e)
        finally:
            cursor.close()
            conexion.close()


def consultar_arriendos():
    conexion = get_conexion()
    resultado = []
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM arriendo;")
            resultado = cursor.fetchall()
        except Exception as e:
            print("Error al consultar arriendos: ", e)
        finally:
            cursor.close()
            conexion.close()
    return resultado


def actualizar_arriendo(id_arrendatario, id_propiedad, fecha_inicio, fecha_termino, monto_pagado):
    conexion = get_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = """UPDATE arriendo
                    SET fecha_inicio = %s, fecha_termino = %s, monto_pagado = %s
                    WHERE id_arrendatario = %s AND id_propiedad = %s"""
            cursor.execute(query, (fecha_inicio, fecha_termino, monto_pagado, id_arrendatario, id_propiedad))
            conexion.commit()
            print("Arriendo actualizado exitosamente.")
        except Exception as e:
            print("Error al actualizar arriendo: ", e)
        finally:
            cursor.close()
            conexion.close()



#CONSULTA ESPECIAL (Punto 5 de la tarea)
#Arrendatarios y dirección de la propiedad con arriendo VIGENTE
# (sin fecha de término, es decir, fecha_termino IS NULL)


def arriendos_vigentes():
    conexion = get_conexion()
    resultado = []
    if conexion:
        try:
            cursor = conexion.cursor()
            query = """
                SELECT a.nombre, p.direccion
                FROM arrendatario a
                JOIN arriendo ar ON a.id_arrendatario = ar.id_arrendatario
                JOIN propiedad p ON ar.id_propiedad = p.id_propiedad
                WHERE ar.fecha_termino IS NULL;
            """
            cursor.execute(query)
            resultado = cursor.fetchall()
        except Exception as e:
            print("Error al consultar arriendos vigentes: ", e)
        finally:
            cursor.close()
            conexion.close()
    return resultado
