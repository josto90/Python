####################
## CLASES/OBJETOS ##
####################

# Casi todo en Python es un objeto, con sus propiedades y métodos.
# Para crear una clase, use la palabra clave class:

class MiClase:
  x = 5

# Crear un objeto
p1 = MiClase()
print(p1.x) 

# La función __init __()
# Los ejemplos anteriores son clases y objetos en su forma más simple, y no son realmente útiles en aplicaciones de la vida real.
# Para comprender el significado de las clases, debemos comprender la función incorporada __init __().
# Todas las clases tienen una función llamada __init __(), que siempre se ejecuta cuando se inicia la clase.
# Use la función __init __() para asignar valores a las propiedades del objeto u otras operaciones que sean necesarias cuando se crea el objeto.
# La función __init __() se llama automáticamente cada vez que se usa la clase para crear un nuevo objeto.

class Persona:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

p1 = Persona("John", 36)

print(p1.nombre)
print(p1.edad) 

# Métodos de un objeto
class Persona:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

  def saludo(self):
    print("Hola, mi nombre es " + self.nombre)

p1 = Persona("John", 36)
p1.saludo() 