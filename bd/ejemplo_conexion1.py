import mysql.connector
#importamos el objeto mysql.connector

conexion = mysql.connector.connect (
    host= "localhost",
    user="root",
    password= "@plvnMYSQL1975"
)
#el nombre conexion se lo doy yo y connect es un metodo del objeto

cursor = conexion.cursor()
#creo la variable cursor, que yo le doy el nombre y cursor() es unmetodo del objeto

cursor.execute("SHOW DATABASES")
for bd in cursor:
    print(bd)
