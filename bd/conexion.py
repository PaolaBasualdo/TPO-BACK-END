import mysql.connector

#diccionario con datos para la conexión con la base de datos
acceso_bd = {"host" : "localhost",
            "user" : "root",
            "password" : "@plvnMYSQL1975",
            "database" : "alphafood"
            }

#clase para trabajar con bases de datos
class BaseDatos:
    def __init__(self, **kwargs):
        self.conector= mysql.connector.connect(**kwargs)
        self.cursor = self.conector.cursor()#se inicializa el cursor al instanciar el objeto

    #metodo para consultar una base de datos 
    def consulta(self, instruccion):
       
        self.cursor.execute(instruccion)
        return self.cursor
    
    #metodos para mostrar las bases de datos que estan el el servidor
    def mostrar_bd(self):
       
        self.cursor.execute("SHOW DATABASES")
        for bd in self.cursor: # type: ignore
            print(bd)
    
    #metodo para  eliminar una base de datos
    def eliminar_bd(self, nombre_bd):
        try:
            self.cursor.execute(f"DROP DATABASE {nombre_bd}")
            print(f"Se eliminó la base de datos correctamente.")
        except:
            print(f"Base de datos '{nombre_bd}' no encontrada.")
            print("Bases de datos en el servidor:")
            self.mostrar_bd()
 #metodo para crear una base de datos
    def eliminar_bd(self, nombre_bd):
        try:
            self.cursor.execute(f"CREATE IF_ DATABASE {nombre_bd}")
            print(f"Se eliminó la base de datos correctamente.")
        except:
            print(f"Base de datos '{nombre_bd}' no encontrada.")
            print("Bases de datos en el servidor:")
            self.mostrar_bd()
    