##############
## FICHEROS ##
##############

# La función clave para trabajar con archivos en Python es la función open(). Toma dos parámetros: nombre de archivo y modo.
# Existen cuatro modos diferentes para abrir un archivo:

# "r" - Leer - Valor predeterminado. Abre un archivo para leer, error si el archivo no existe
# "a" - Agregar - Abre un archivo para agregar, crea el archivo si no existe
# "w" - Escribir - Abre un archivo para escribir, crea el archivo si no existe
# "x" - Crear - Crea el archivo especificado, devuelve un error si el archivo existe

# Además, puede especificar si el archivo debe manejarse en modo binario o de texto

# "t" - Texto - Valor predeterminado. Modo de texto
# "b" - Binario - Modo binario (por ejemplo, imágenes)

f = open("demofile.txt", "rt") # rt son valores por defecto. No es necesario especificarlos.
f.close() 

f = open("demofile.txt", "r")
print(f.read()) 
f.close() 

print()

# Devolver un número concreto de caracteres
f = open("demofile.txt", "r")
print(f.read(5)) 
f.close() 

print()

# Leer líneas
f = open("demofile.txt", "r")
print(f.readline()) 
f.close() 

print()

f = open("demofile.txt", "r")
for x in f:
  print(x) 
f.close() 

# Con "a" agregas al final del fichero:

f = open("demofile.txt", "a")
f.write("Nuevo contenido")
f.close()

f = open("demofile.txt", "r")
print(f.read())
f.close()

print()

# Con "w" sobreescribes el contenido:
f = open("demofile.txt", "w")
f.write("El contenido ha sido borrado")
f.close()

f = open("demofile.txt", "r")
print(f.read()) 
f.close()

# Para eliminar un archivo, debe importar el módulo del sistema operativo y ejecutar su función os.remove():
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist") 