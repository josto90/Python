############
## ARRAYS ##
############

# Existen cuatro tipos de arrays en el lenguaje de programación Python:

#  * Lista: Es una colección ordenada y mutable. Permite duplicados.
#  * Tupla: Es una colección ordenada e inmutable. Permite duplicados.
#  * Conjunto: Es una colección que no está ordenada ni indexada. No hay duplicados.
#  * Diccionario: Es una colección desordenada, modificable e indexada. No hay miembros duplicados.


############
## LISTAS ##
############

# Crear una lista
lista = ["manzana", "plátano", "cereza"]
print(lista)

lista = list(("manzana", "plátano", "cereza")) # Mediante el constructor
print(lista)
print()

# Acceso a un elemento
lista = ["manzana", "plátano", "cereza"]
print(lista[1])

print()

# Acceso al último elemento
lista = ["manzana", "plátano", "cereza"]
print(lista[-1])

print()

# Rango de elementos. 
lista = ["manzana", "plátano", "cereza", "naranja", "kiwi", "melón", "mango"]
print(lista[2:5])  # El elemento 5 no es incluido
print(lista[:4])   # Muestra desde el primer elemento al 4(no incluido)
print(lista[2:])   # Muestra desde el elemento 2 al final.

print()

# Cambio de un valor de la lista
lista = ["manzana", "plátano", "cereza"]
lista[1] = "sandía"
print(lista)

print()

# Recorrer una lista
lista = ["manzana", "plátano", "cereza"]
for x in lista:
  print(x) 

print()

# Comprobar si un elemento existe en una lista
lista = ["manzana", "plátano", "cereza"]
if "manzana" in lista:
  print("Si, existe") 

print()

# Tamaño de una lista
lista = ["manzana", "plátano", "cereza"]
print(len(lista))

print()

# Manipular listas
lista = ["manzana", "plátano", "cereza"]
lista.append("naranja")  # Inserción al final
print(lista)
lista.insert(1, "melón") # Inserción en una posición
print(lista)
lista.remove("plátano")  # Elimina un elemento
print(lista)
lista.pop()			     # Elimina el último elemento
print(lista)
del lista[0]			 # Elimina un elemento por índice
print(lista)
lista.clear()			 # Vacía la lista
print(lista)
del lista                # Elimina la lista

print()

# Copiar listas
# No se puede copiar una lista simplemente escribiendo list2 = list1
# list2 solo será una referencia a list1, y los cambios realizados en list1 también se realizarán automáticamente en list2.
lista = ["manzana", "plátano", "cereza"]
lista2 = lista.copy()
print(lista2)

lista3 = list(lista)
print(lista3)

print()

# Unión de dos listas
lista = ["manzana", "plátano", "cereza"]
lista2 = ["manzana", "plátano", "cereza"]
lista3 = lista + lista2
print(lista3)

lista = ["manzana", "plátano", "cereza"]
lista2 = ["manzana", "plátano", "cereza"]
for x in lista2:
  lista.append(x)

print(lista)

lista = ["manzana", "plátano", "cereza"]
lista2 = ["manzana", "plátano", "cereza"]
lista.extend(lista2)
print(lista)

print()

# Algunos método útiles de listas:
append()	# Agrega un elemento al final de la lista
clear()		# Elimina todos los elementos de la lista.
copy()		# Devuelve una copia de la lista.
count()		# Devuelve el número de elementos con el valor especificado.
extend()	# Agrega los elementos de una lista (o cualquier iterable) al final de la lista actual
index()		# Devuelve el índice del primer elemento con el valor especificado
insert()	# Agrega un elemento en la posición especificada
pop()		# Elimina el elemento en la posición especificada.
remove()	# Elimina el elemento con el valor especificado.
reverse()	# Invierte el orden de la lista
sort()		# Ordena la lista