###############
## FUNCIONES ##
###############


# Se definen con la palabra def
def mi_funcion():
  print("Hola mundo") 

mi_funcion()

print()

# Paso de parámetros
def mi_funcion(nombre):
  print(nombre + " Refsnes")

mi_funcion("Emil")

print()

# Número de argumentos desconocido
def mi_funcion(*niños):
  print("El niño mas joven es " + niños[2])

mi_funcion("Emil", "Tobias", "Linus") 

print()

# Argumentos pasados como clave:valor
def mi_funcion(niño3, niño2, niño1):
  print("El niño mas joven es " + niño3)

mi_funcion(niño1 = "Emil", niño2 = "Tobias", niño3 = "Linus") 

print()

# Argumentos pasados como clave:valor desconocidos
def mi_funcion(**niño):
  print("Su apellido es " + niño["lname"])

mi_funcion(fname = "Tobias", lname = "Refsnes") 

print()

# Devolver valores

def mi_funcion(x):
  return 5 * x

# Pasar para que no de error
def mi_funcion():
  pass

# Recursión
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

tri_recursion(6)