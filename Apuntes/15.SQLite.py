############
## SQLITE ##
############
# Con https://sqlitebrowser.org se puede abrir la BBDD creada y comprobar los datos
# Conectarse a una BBDD
import sqlite3
conexion = sqlite3.connect("Pruebadb.db") # Sino existe la crea
conexion.close()

# Crear una tabla
import sqlite3
conexion = sqlite3.connect("Pruebadb.db")
cursor = conexion.cursor()
cursor.execute("DROP TABLE PERSONAS") # Por si existe
cursor.execute("CREATE TABLE PERSONAS(nombre TEXT, apellido1 TEXT, apellido2 TEXT, edad INTEGER)")

conexion.commit()
conexion.close()

# Insertar datos
import sqlite3
conexion = sqlite3.connect("Pruebadb.db")
cursor = conexion.cursor()
cursor.execute("INSERT INTO PERSONAS VALUES('Antonio', 'Perez', 'Gomez', 35)")

conexion.commit()
conexion.close()

# Insertar varios registros
import sqlite3
conexion = sqlite3.connect("Pruebadb.db")
cursor = conexion.cursor()

lista_personas = [('Pedro','Rodriguez','Perez',35), ('Juan','Ibañez','Lopez',40), ('Daniel','Rodriguez','Gonzalez',30)]
cursor.executemany("INSERT INTO PERSONAS VALUES (?,?,?,?)", lista_personas)
conexion.commit()
conexion.close()

# Consultar datos
import sqlite3
conexion = sqlite3.connect("Pruebadb.db")
cursor = conexion.cursor()
cursor.execute("SELECT * FROM PERSONAS")
personas = cursor.fetchall() # fetchall recoge los resultados de la sentencia anterior
for persona in personas:
		print(persona)
conexion.close()