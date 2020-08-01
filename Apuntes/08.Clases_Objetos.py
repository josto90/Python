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

# -------------------------------------------------------
# Primer argumento self
# Los objetos tienen una característica muy importante: son conscientes de que existen. Y no, no es broma.
# Cuando se ejecuta un método desde un objeto (que no desde una clase), 
# se envía un primer argumento implícito que hace referencia al propio objeto. 
# Si lo definimos en nuestro método podremos capturarlo y ver qué es:

class Galleta:
    chocolate = False

    def saludar(soy_el_propio_objeto): # Equivalente a poner self
        print("Hola, soy una galleta muy sabrosa")
        print(soy_el_propio_objeto)

galleta = Galleta()
galleta.saludar()
print(galleta)

# El parámetro self es una referencia a la instancia actual de la clase y se usa para acceder a las variables que pertenecen a la clase.
# No tiene que llamarse self, puede llamarlo como quiera, pero tiene que ser el primer parámetro de cualquier función en la clase.

# --------------------------------------------------------
# --------------------------------------------------------
## Métodos especiales
# Se llaman especiales porque la mayoría ya existen de forma oculta y sirven para tareas específicas.
# Constructor
# El constructor es un método que se llama automáticamente al crear un objeto, se define con el nombre init:

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



# Destructor
# Si existe un constructor también debe existir un destructor que se llame al eliminar el objeto 
# para que encargue de las tareas de limpieza como vaciar la memoria. Ese es el papel del método especial del. 
# Es muy raro sobreescribir este método porque se maneja automáticamente, pero es interesante saber que existe.
# Todos los objetos se borran automáticamente de la memoria al finalizar el programa, 
# aunque también podemos eliminarlos automáticamente pasándolos a la función del():

class Galleta:

    def __del__(self):
        print("La galleta se está borrando de la memoria")

galleta = Galleta()

del(galleta)

# En este punto vale comentar algo respecto a los métodos especiales como éste, 
# y es que pese a que tienen accesores en forma de función para facilitar su llamada, 
# es totalmente posible ejecutarlos directamente como si fueran métodos normales.


# String

# El método str es el que devuelve la representación de un objeto en forma de cadena. 
# Un momento en que se llama automáticamente es cuando imprimirmos una variable por pantalla.
# Por defecto los objetos imprimen su clase y una dirección de memoria, 
# pero eso puede cambiarse sobreescribiendo el comportamiento.

class Galleta:

    def __init__(self, sabor, color):
        self.sabor = sabor
        self.color = color

    def __str__(self):
       return f"Soy una galleta {self.color} y {self.sabor}."

galleta = Galleta("dulce", "blanca")

print(galleta)
print(str(galleta))
print(galleta.__str__())

# Length

# Finalmente otro método especial interesante es el que devuelve la longitud.
# Normalmente está ligado a colecciones, pero nada impide definirlo en una clase.
# Y sí, digo definirlo y no redefinirlo porque por defecto no existe en los objetos aunque sea el que se ejecuta
# al pasarlos a la función len().

class Cancion:

    def __init__(self, autor, titulo, duracion):  # en segundos
        self.duracion = duracion

    def __len__(self):
       return self.duracion

cancion = Cancion("Queen", "Don't Stop Me Now", 210)

print(len(cancion))
print(cancion.__len__())
# --------------------------------------------------------


# Modificar propiedades del objeto
p1.edad = 40

# Eliminar propiedades del objeto
del p1.edad

# Eliminar el objeto
del p1 

# --------------------------------------------------------
## Encapsulación

# La encapsulación consiste en denegar el acceso a los atributos y métodos internos de la clase desde el exterior.
# En Python no existe, pero se puede simular precediendo atributos y métodos con dos barras bajas __ 
# como indicando que son "especiales".

class Ejemplo:
    __atributo_privado = "Soy un atributo inalcanzable desde fuera."

e = Ejemplo()
# print(e.__atributo_privado) daría error

class Ejemplo:
    def __metodo_privado(self):
        print("Soy un método inalcanzable desde fuera.")

e = Ejemplo()
# e.__metodo_privado() daría error

# --------------------------------------------------------

## Herencia

# La herencia nos permite definir una clase que hereda todos los métodos y propiedades de otra clase.
# La clase padre es la clase de la que se hereda, también llamada clase base.
# La clase secundaria es la clase que hereda de otra clase, también llamada clase derivada. 

class Persona:
  def __init__(self, nombre, apellidos):
    self.nombre = nombre
    self.apellidos = apellidos

  def imprimirnombre(self):
    print(self.nombre, self.apellidos)

x = Persona("John", "Doe")
x.imprimirnombre() 

# Clase hijo:

class Estudiante(Persona):
 	pass 

x = Estudiante("Mike", "Olsen")
x.imprimirnombre()

# Cuando agrega la función __init__(), la clase secundaria ya no heredará la función __init__() de los padres (override).
# Para mantener la herencia de la función __init __ () del padre, agregue una llamada a la función __init__() del padre:


class Estudiante(Persona):
  def __init__(self, nombre, apellidos):
  	 Persona.__init__(self, nombre, apellidos) 

x = Estudiante("Mike", "Olsen")
x.imprimirnombre()

# Python también tiene una función super() que hará que la clase hija herede todos los métodos y propiedades de su padre:
# Al usar la función super(), no tiene que usar el nombre del elemento padre, heredará automáticamente los métodos y propiedades de su padre.
class Estudiante(Persona):
  def __init__(self, nombre, apellidos):
  	 super().__init__(nombre, apellidos) 

y = Estudiante("Super", "Prueba")
y.imprimirnombre()

# Añadimos una propiedad y un método a la clase hija
class Estudiante(Persona):
  def __init__(self, nombre, apellidos, año):
  	super().__init__(nombre, apellidos) 
  	self.año = año

  def bienvenido(self):
    print("Bienvenido", self.nombre, self.apellidos, "del año", self.año)

y = Estudiante("Super", "Prueba", 2019)
y.bienvenido()


