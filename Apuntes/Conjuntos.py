############
## ARRAYS ##
############

# Existen cuatro tipos de arrays en el lenguaje de programación Python:

#  * Lista: Es una colección ordenada y mutable. Permite duplicados.
#  * Tupla: Es una colección ordenada e inmutable. Permite duplicados.
#  * Conjunto: Es una colección que no está ordenada ni indexada. No hay duplicados.
#  * Diccionario: Es una colección desordenada, modificable e indexada. No hay miembros duplicados.

##############
## CONJUNTO ##
##############

# Crear un conjunto
set1 = {"manzana", "plátano", "cereza"}
print(set1)

print()

# Acceder a los elementos de un conjunto. Como no tiene índice, no se puede acceder a un elemento concreto.
set1 = {"manzana", "plátano", "cereza"}

for x in set1:
  print(x) 

print()

# Comprobar si un elemento esta en un conjunto.
set1 = {"manzana", "plátano", "cereza"}

print("cereza" in set1)

print()

 
