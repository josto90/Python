##########
## DATE ##
##########

# Una fecha en Python no es un tipo de datos propio, pero podemos importar un módulo llamado datetime para trabajar con fechas como objetos de fecha.

import datetime

x = datetime.datetime.now()
print(x) 

print()
# El método strftime() permite dar formato a la cadena devuelta:
import datetime

y = datetime.datetime.now()
print(y.strftime("%B")) 

# Referencia a todos los formatos:
# https://www.w3schools.com/python/python_datetime.asp

##########
## MATH ##
##########

# Python tiene un conjunto de funciones matemáticas integradas, incluido un extenso módulo matemático, que le permite realizar tareas matemáticas en números.

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

print()
# Python también tiene un módulo incorporado llamado matemáticas, que amplía la lista de funciones matemáticas.
import math
x = math.sqrt(64)
print(x) 

print()

import math
x = math.pi
print(x)
# Referencia a todas las funciones:
# https://www.w3schools.com/python/module_math.asp
