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

# Añadir un elemento a un conjunto.
set1 = {"manzana", "plátano", "cereza"}

set1.add("naranja")

print(set1) 

print() 

# Añadir múltiples elementos a un conjunto.
set1 = {"manzana", "plátano", "cereza"}

set1.update(["naranja", "mango", "uvas"])

print(set1)
print() 

# Eliminar elementos de un conjunto.
set1 = {"manzana", "plátano", "cereza"}
set1.remove("plátano")    # Remove devuelve error si el elemento no existe. Discard no.
set1.discard("cereza")
set1.pop() 				  # Elimina el último elemento
set1.clear()			  # Vacía el conjunto.

print(set1)
print() 

# Unión de conjuntos.

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)   # Unión crea un nuevo conjunto resultado.
print(set3) 

set1.update(set2)		  # Update añade los elementos de un conjunto a otro.
print(set1) 

# Constructor set

set1 = set(("manzana", "plátano", "cereza")) 
print(set1) 