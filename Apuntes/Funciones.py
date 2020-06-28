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
