# Tarea Práctica - Base de Datos (Arriendos)

Aplicación en Python que se conecta a una base de datos PostgreSQL para gestionar
Arrendatarios, Propiedades y Arriendos, cumpliendo con los puntos solicitados en la
Tarea Práctica de Base de Datos (Junio 2026).

## Estructura del proyecto

```
├── database.py          # Conexión a PostgreSQL y creación de tablas
├── crud_operations.py   # Funciones CRUD (insertar, consultar, actualizar)
├── app.py                # Menú principal / interfaz de la aplicación
└── README.md
```

## Modelo Relacional

- **arrendatario** (id_arrendatario PK, nombre, ciudad, telefono)
- **propiedad** (id_propiedad PK, direccion, tipo_propiedad, valor_mensual)
- **arriendo** (id_arrendatario PK/FK, id_propiedad PK/FK, fecha_inicio, fecha_termino, monto_pagado)

Un arriendo se considera **vigente** cuando `fecha_termino` está vacía (NULL).

## Requisitos previos

- Python 3.10+
- PostgreSQL instalado y corriendo
- Una base de datos ya creada (por ejemplo `Tarea_Python`)

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/RenatoKeso/PROYECTOTAREABASEDEDATOS.git
   cd PROYECTOTAREABASEDEDATOS
   ```

2. Crear y activar un entorno virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```

3. Instalar dependencias:
   ```bash
   python -m pip install psycopg2-binary
   ```

## Configuración de la base de datos

Abrir `database.py` y ajustar los datos de conexión con los de tu PostgreSQL local:

```python
conexion = psycopg2.connect(
    database='Tarea_Python',   # nombre de tu base de datos
    user='postgres',           # usuario de PostgreSQL
    password='TU_PASSWORD',    # contraseña de tu usuario
    host='localhost',
    port='5432'
)
```

## Uso

1. **Crear las tablas** (solo la primera vez, o si aún no existen):
   ```bash
   python database.py
   ```
   Debe mostrar: `Tablas creadas correctamente (o ya existían).`

2. **Ejecutar la aplicación:**
   ```bash
   python app.py
   ```

3. En el **Menú Principal** puedes:
   - `1` Gestionar Arrendatarios (insertar, consultar, actualizar)
   - `2` Gestionar Propiedades (insertar, consultar, actualizar)
   - `3` Gestionar Arriendos (insertar, consultar, actualizar)
   - `4` Ver Arriendos Vigentes — consulta que muestra nombre del arrendatario
     y dirección de la propiedad para los arriendos sin fecha de término
   - `5` Salir

> Nota: al insertar un arriendo, si se deja la **fecha de término vacía**
> (solo presionar Enter), el arriendo queda registrado como vigente.

## Puntos de la tarea cubiertos

| Punto | Descripción                                             | Dónde                                  |
|-------|----------------------------------------------------------|-----------------------------------------|
| 1     | Desarrollo en Python con PostgreSQL                      | `database.py`, `crud_operations.py`     |
| 2     | Interfaz de acceso a los puntos 3, 4 y 5                 | `app.py` (menú principal)               |
| 3     | Ingresar datos mediante formulario                        | Opción "Insertar" en cada submenú       |
| 4     | Modificar datos (consultando previamente los existentes) | Opción "Actualizar" en cada submenú     |
| 5     | Consulta de arriendos vigentes                            | Opción 4 del menú principal             |