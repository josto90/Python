############
## ARRAYS ##
############

# Existen cuatro tipos de arrays en el lenguaje de programación Python:

#  * Lista: Es una colección ordenada y mutable. Permite duplicados.
#  * Tupla: Es una colección ordenada e inmutable. Permite duplicados.
#  * Conjunto: Es una colección que no está ordenada ni indexada. No hay duplicados.
#  * Diccionario: Es una colección desordenada, modificable e indexada. No hay miembros duplicados.

#################
## DICCIONARIO ##
#################

# Crear un diccionario
diccionario =	{
  "marca": "Ford",
  "modelo": "Mustang",
  "año": 1964
}
print(diccionario)

print()

# Acceder a un ítem
x = diccionario["modelo"]
print(x)

x = diccionario.get("modelo")
print(x)

print()

# Modificar un valor
diccionario["año"] = 2018
print(diccionario)

print()

# Recorrer un diccionario
for x in diccionario:
  print(diccionario[x]) 

for x in diccionario.values():
  print(x)

print()

# Recorrer un diccionario mostrando clave:valor
for x, y in diccionario.items():
  print(x, y) 

print()

# Comprobar si una clave existe
diccionario =	{
  "marca": "Ford",
  "modelo": "Mustang",
  "año": 1964
}
if "modelo" in diccionario:
  print("Si, 'modelo' es una de las claves") 

print()

# Número de items del diccionario
print(len(diccionario)) 

print()


# Añadir items al diccionario
diccionario =	{
  "marca": "Ford",
  "modelo": "Mustang",
  "año": 1964
}
diccionario["color"] = "rojo"
print(diccionario)

print()