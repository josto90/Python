############
## ARRAYS ##
############

# Existen cuatro tipos de arrays en el lenguaje de programación Python:

#  * Lista: Es una colección ordenada y mutable. Permite duplicados.
#  * Tupla: Es una colección ordenada e inmutable. Permite duplicados.
#  * Set: Es una colección que no está ordenada ni indexada. No hay duplicados.
#  * Diccionario: Es una colección desordenada, modificable e indexada. No hay miembros duplicados.

############
## TUPLAS ##
############

# Crear una tupla
tupla = ("manzana", "plátano", "cereza")
print(tupla)

print()

# Acceso a sus elementos
tupla = ("manzana", "plátano", "cereza","kiwi", "melon", "mango")
print(tupla[1])
print(tupla[-1])
print(tupla[2:5])
print(tupla[-4:-1])
print()

# Modificar una tupla. Al ser inmutable, hay que convertirla en una lista.
x = ("manzana", "plátano", "cereza")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x) 

print()

# Recorrer una tupla
tupla = ("manzana", "plátano", "cereza")
for x in tupla:
  print(x)

print()

# Comprobar si un item existe en una tupla
tupla = ("manzana", "plátano", "cereza")
if "manzana" in tupla:
  print("Sí, existe") 

print()

# Constructor tuple()

tupla = tuple(("manzana", "plátano", "cereza")) # doble paréntesis
print(tupla)