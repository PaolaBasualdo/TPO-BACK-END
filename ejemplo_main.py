from connection import *

# funciones  
def validar():
    return len(dni.get()) > 0 and len(legajo.get()) > 0 and len(nombre.get()) > 0 and len(apellido.get()) > 0
    
def limpiar():
    dni.set("")
    legajo.set("")
    nombre.set("")
    apellido.set("")
    dni_entry.config(state="normal")
    
    
def seleccionar(event):
    seleccion = tabla_estud.selection()
    if seleccion:
        id_db = seleccion[0]
        values = tabla_estud.item(id_db, "values")
        if values:
            dni.set(values[1])
            legajo.set(values[2])
            nombre.set(values[3])
            apellido.set(values[4])
    
def vaciar_datos():
    #se deben recorrer las filas del treeview y borrar los datos
    filas = tabla_estud.get_children()
    for fila in filas:
        tabla_estud.delete(fila)

def cargar_datos():
    vaciar_datos()
    sql = "SELECT * FROM alumnos"
    db.cursor.execute(sql)
    filas = db.cursor.fetchall()
    for fila in filas:
      id_db = fila[0]
      tabla_estud.insert("", END, id_db, text=id_db, values=fila)
    
def eliminar():
    respuesta = messagebox.askquestion("Eliminar", message="¿Estás seguro de eliminar el registro seleccionado?")
    if respuesta == "yes":
        try:
            id_db = tabla_estud.selection()[0]
            sql = "DELETE FROM alumnos WHERE IdAlumno=" + id_db
            db.cursor.execute(sql)
            db.connection.commit()
            tabla_estud.delete(id_db)
            mensaje_label.config(text="Registro eliminado correctamente", fg="green")
            cargar_datos()
            limpiar()
        except IndexError:
            mensaje_label.config(text="Seleccione un registro para eliminar", fg="red")

def agregar():
    respuesta = messagebox.askquestion("Agregar", message="¿Estás seguro de agregar el nuevo registro?")
    if respuesta == "yes":
        if validar():
          values = (dni.get(), legajo.get(), nombre.get(), apellido.get())
          sql = "INSERT INTO alumnos (Dni, Legajo, Nombre, Apellido) VALUES (%s, %s,%s, %s)" #comodines
          db.cursor.execute(sql, values)
          db.connection.commit()
          mensaje_label.config(text="Registro añadido correctamente", fg="green")
          cargar_datos()
          limpiar()
        else:
          mensaje_label.config(text="Los campos no deben estar vacíos", fg="red")   

def actualizar():
	respuesta = messagebox.askquestion("Actualizar", message="¿Estás seguro de actualizar el registro seleccionado?")
	if respuesta == "yes":
		if validar():  
			id_db = tabla_estud.selection()[0]
			values = (dni.get(), legajo.get(), nombre.get(), apellido.get())
			sql = "UPDATE alumnos SET Dni=%s, Legajo=%s, Nombre=%s, Apellido=%s WHERE IdAlumno="+id_db #comodines
			db.cursor.execute(sql, values)
			db.connection.commit()
			mensaje_label.config(text="Registro actualizado correctamente", fg="green")
			limpiar()
			cargar_datos()
		else:
			mensaje_label.config(text="Los campos no deben estar vacíos", fg="red")