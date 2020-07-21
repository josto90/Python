#################
## EXCEPCIONES ##
#################

# El bloque "try" le permite probar un bloque de código en busca de errores.
# El bloque "except" le permite manejar el error.
# El bloque "finally" le permite ejecutar código, independientemente del resultado de los bloques try y except.

# Utilización de varios except:
try:
  print(x)
except NameError:
  print("La Variable no está definida")
except:
  print("Algo ha ido mal")

print()
  # Utilización de else:
try:
  print("Hola")
except:
	print("Algo ha ido mal")
else:
 	print("Todo ha ido bien")

print()

# Utilización de finally:
try:
  print(x)
except:
  print("Algo ha ido mal")
finally:
  print("El bloque 'try except' ha terminado")

print()

# Puede ser muy útil para acciones como cerrar ficheros

try:
  f = open("demofile.txt")
  f.write("Lorum Ipsum")
except:
  print("Algo ha ido mal")
finally:
  f.close()

# Como desarrollador de Python, puede elegir lanzar una excepción si se produce una condición.
# Para lanzar una excepción, use la palabra clave raise

x = -1

if x < 0:
  raise Exception("Números menores de 0 no permitidos") 