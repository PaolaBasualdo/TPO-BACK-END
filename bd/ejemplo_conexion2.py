import mysql.connector

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="@plvnMSQL1975",
            database="alphafood"
        ) #datos de la conexion
        self.cursor = self.connection.cursor() #para ejecutar las consultas