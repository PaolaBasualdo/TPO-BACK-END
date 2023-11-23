import bd.conexion as sqlbd

#instancio el objeto base_datos de la Clase BaseDatos que esta en el archivo connection
base_datos = sqlbd.BaseDatos(**sqlbd.acceso_bd)

base_datos.mostrar_bd()

