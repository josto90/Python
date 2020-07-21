##########
## JSON ##
##########

# Python tiene un paquete incorporado llamado json, que puede usarse para trabajar con datos JSON.

import json

# Si tiene un JSON, puede convertirlo en un diccionario de python json.loads().
import json

x =  '{ "nombre":"John", "edad":30, "ciudad":"New York"}'
y = json.loads(x) # Genera en y un diccionario
print(y["edad"]) 

print()
# Si tiene un objeto Python, puede convertirlo en una cadena JSON utilizando el método json.dumps()

import json

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

y = json.dumps(x)
print(y) 

# Se pueden convertir objetos de Python de los siguientes tipos en cadenas JSON:

#   dicccionario
#   lista
#   tupla
#   string
#   int
#   float
#   Boolean
import json

print(json.dumps({"nombre": "John", "edad": 30}))
print(json.dumps(["manzana", "plátano"]))
print(json.dumps(("manzana", "plátano")))
print(json.dumps("hola"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None)) 

print()

# Se puede formatear el resultado:
import json

x = {
  "nombre": "John",
  "edad": 30,
  "casado": True,
  "divorciado": False,
  "hijos": ("Ann","Billy"),
  "mascotas": None,
  "coches": [
    {"modelo": "BMW 230", "mpg": 27.5},
    {"modelo": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4))
print()

# También se pueden definir los separadores:
print(json.dumps(x, indent=4, separators=(". ", " = ")))

# Por otro lado, se pueden ordenar los resultados:

print(json.dumps(x, indent=4, sort_keys=True))