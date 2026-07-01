# ARCHIVO PRINCIPAL DE LA APLICACIÓN
# Menú por consola para gestionar Arrendatarios, Propiedades y Arriendos.

from crud_operations import (
    insertar_arrendatario, consultar_arrendatarios, actualizar_arrendatario,
    insertar_propiedad, consultar_propiedades, actualizar_propiedad,
    insertar_arriendo, consultar_arriendos, actualizar_arriendo,
    arriendos_vigentes
)


# ---------------------------------------------------------
# GESTIÓN DE ARRENDATARIOS
# ---------------------------------------------------------
def gestionar_arrendatarios():
    while True:
        menu = """
        \n---- Gestión de Arrendatarios ----
        \n1. Insertar Arrendatario
        \n2. Consultar Arrendatarios
        \n3. Actualizar Arrendatario
        \n4. Volver al Menú Principal
        """
        print(menu)
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_arrendatario = int(input("ID: "))
            nombre = input("Nombre: ")
            ciudad = input("Ciudad: ")
            telefono = input("Teléfono: ")
            insertar_arrendatario(id_arrendatario, nombre, ciudad, telefono)

        elif opcion == "2":
            print("\nARRENDATARIOS REGISTRADOS:")
            for a in consultar_arrendatarios():
                print(a)

        elif opcion == "3":
            # Primero se muestran los datos existentes, como pide el punto 4 de la tarea
            print("\nARRENDATARIOS REGISTRADOS:")
            for a in consultar_arrendatarios():
                print(a)

            id_arrendatario = int(input("\nID del arrendatario a modificar: "))
            nombre = input("Nuevo nombre: ")
            ciudad = input("Nueva ciudad: ")
            telefono = input("Nuevo teléfono: ")
            actualizar_arrendatario(id_arrendatario, nombre, ciudad, telefono)

        elif opcion == "4":
            break
        else:
            print("Opción no válida, intente nuevamente.")


# ---------------------------------------------------------
# GESTIÓN DE PROPIEDADES
# ---------------------------------------------------------
def gestionar_propiedades():
    while True:
        menu = """
        \n---- Gestión de Propiedades ----
        \n1. Insertar Propiedad
        \n2. Consultar Propiedades
        \n3. Actualizar Propiedad
        \n4. Volver al Menú Principal
        """
        print(menu)
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_propiedad = int(input("ID: "))
            direccion = input("Dirección: ")
            tipo_propiedad = input("Tipo de propiedad: ")
            valor_mensual = float(input("Valor mensual: "))
            insertar_propiedad(id_propiedad, direccion, tipo_propiedad, valor_mensual)

        elif opcion == "2":
            print("\nPROPIEDADES REGISTRADAS:")
            for p in consultar_propiedades():
                print(p)

        elif opcion == "3":
            print("\nPROPIEDADES REGISTRADAS:")
            for p in consultar_propiedades():
                print(p)

            id_propiedad = int(input("\nID de la propiedad a modificar: "))
            direccion = input("Nueva dirección: ")
            tipo_propiedad = input("Nuevo tipo de propiedad: ")
            valor_mensual = float(input("Nuevo valor mensual: "))
            actualizar_propiedad(id_propiedad, direccion, tipo_propiedad, valor_mensual)

        elif opcion == "4":
            break
        else:
            print("Opción no válida, intente nuevamente.")


# ---------------------------------------------------------
# GESTIÓN DE ARRIENDOS
# ---------------------------------------------------------
def gestionar_arriendos():
    while True:
        menu = """
        \n---- Gestión de Arriendos ----
        \n1. Insertar Arriendo
        \n2. Consultar Arriendos
        \n3. Actualizar Arriendo
        \n4. Volver al Menú Principal
        """
        print(menu)
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_arrendatario = int(input("ID Arrendatario: "))
            id_propiedad = int(input("ID Propiedad: "))
            fecha_inicio = input("Fecha inicio (AAAA-MM-DD): ")
            fecha_termino = input("Fecha término (AAAA-MM-DD, dejar vacío si vigente): ")
            fecha_termino = fecha_termino if fecha_termino.strip() != "" else None
            monto_pagado = float(input("Monto pagado: "))
            insertar_arriendo(id_arrendatario, id_propiedad, fecha_inicio, fecha_termino, monto_pagado)

        elif opcion == "2":
            print("\nARRIENDOS REGISTRADOS:")
            for a in consultar_arriendos():
                print(a)

        elif opcion == "3":
            print("\nARRIENDOS REGISTRADOS:")
            for a in consultar_arriendos():
                print(a)

            id_arrendatario = int(input("\nID Arrendatario: "))
            id_propiedad = int(input("ID Propiedad: "))
            fecha_inicio = input("Nueva fecha inicio (AAAA-MM-DD): ")
            fecha_termino = input("Nueva fecha término (AAAA-MM-DD, dejar vacío si vigente): ")
            fecha_termino = fecha_termino if fecha_termino.strip() != "" else None
            monto_pagado = float(input("Nuevo monto pagado: "))
            actualizar_arriendo(id_arrendatario, id_propiedad, fecha_inicio, fecha_termino, monto_pagado)

        elif opcion == "4":
            break
        else:
            print("Opción no válida, intente nuevamente.")


# ---------------------------------------------------------
# CONSULTA ESPECIAL (Punto 5)
# ---------------------------------------------------------
def mostrar_arriendos_vigentes():
    print("\n---- Arrendatarios con arriendo VIGENTE ----")
    resultados = arriendos_vigentes()
    if resultados:
        for nombre, direccion in resultados:
            print(f"Arrendatario: {nombre} | Propiedad: {direccion}")
    else:
        print("No hay arriendos vigentes en este momento.")


# ---------------------------------------------------------
# MENÚ PRINCIPAL
# ---------------------------------------------------------
def main_menu():
    while True:
        menu_principal = """
        \n---- Menú Principal ----
        \n1. Gestionar Arrendatarios
        \n2. Gestionar Propiedades
        \n3. Gestionar Arriendos
        \n4. Ver Arriendos Vigentes (Consulta especial)
        \n5. Salir
        """
        print(menu_principal)
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            gestionar_arrendatarios()
        elif opcion == "2":
            gestionar_propiedades()
        elif opcion == "3":
            gestionar_arriendos()
        elif opcion == "4":
            mostrar_arriendos_vigentes()
        elif opcion == "5":
            print("Saliendo de la aplicación...")
            break
        else:
            print("Opción no válida, intente nuevamente.")


if __name__ == "__main__":
    main_menu()
