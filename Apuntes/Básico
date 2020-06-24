###############
## VARIABLES ##
###############

 #Reglas para las variables de Python:

    # Un nombre de variable debe comenzar con una letra o el carácter de subrayado
    # Un nombre de variable no puede comenzar con un número
    # Un nombre de variable solo puede contener caracteres alfanuméricos y guiones bajos (A-z, 0-9 y _)
    # Los nombres de las variables distinguen entre mayúsculas y minúsculas (edad, edad y EDAD son tres variables diferentes)

#Legales:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Ilegales:
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# Asignación múltiple de valores a variables
x, y, z = "Naranja", "Plátano", "Cereza"

# Combinación de variables
x = "awesome"
print("Python is " + x)

x = "Python is "
y = "awesome"
z =  x + y
print(z)

print()

# Las variables pueden ser globales o locales
# Si utilizas la key global, una variable dentro de una función se transforma en global.
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) 

print()

# Para cambiar el valor de una variable global dentro de una función, consulte la variable usando la palabra clave global:

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) 

print()

#############
## NUMEROS ##
#############

# Hay tres tipos numéricos: int, float, complex
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convertir de int a float:
a = float(x)

#convert de float a int:
b = int(y)

#convert de int a complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c)) 

print()  

#############
## CASTING ##
#############

# la conversión en python se realiza mediante funciones de constructor:

int()
float() 
str()

###############
## BOOLEANOS ##
###############
# Con la función bool() puedes evaluar cualquier valor, devolviendo true o false
# Cualquier string es True, excepto las vacías. Lo mismo ocurre con las listas, tuplas, sets y diccionarios. En el caso de los números, solo es false el 0.

print(bool("Hello"))
print(bool(15))

print()  

# Python también tiene muchas funciones integradas que devuelven un valor booleano, como la función isinstance (),
# que se puede usar para determinar si un objeto es de cierto tipo de datos:

x = 200
print(isinstance(x, int)) 

print()  

########
## IF ##
########

a = 100
b = 10
if b > a:
  print("b es mayor que a")
elif a == b:
  print("a y b son iguales")
else:
  print("a es mayor que b")

#########
## FOR ##
#########

#FOR básico
lista = ["uno", "dos", "tres"]
for item in lista:
  print(item)

print()  

#FOR con ELSE
for x in range(6):
  print(x)
else:
  print("Bucle terminado") 

print()  

#pass permite pasar una iteración de un bucle
for x in [0, 1, 2]:
  pass

print()  

#break permite salir del bucle
frutas = ["manzana", "plátano", "melón"]
for x in frutas:
  print(x)
  if x == "plátano":
    break

print()  

#Continue permite saltar esa iteracción
frutas = ["manzana", "plátano", "melón"]
for x in frutas:
  
  if x == "plátano":
    continue
  print(x)
  
print() 

#############
## RANGE() ##
#############
#Range es una función que crea una lista de elementos del primer elemento específicado(0 por defecto) a n-1 del segundo elemento indicado, con una secuencia indicada(1 por defecto).

#RANGE sin especificar elemento inicial
for x in range(5):
  print(x) 

print()  

#RANGE Especificando elemento inicial
for x in range(2,5):
  print(x) 

print()  

#RANGE con secuencia diferente a 1
for x in range(2, 10, 3):
  print(x)

print() 

###########
## WHILE ##
###########

i = 1
while i < 6:
  print(i)
  i += 1


####################
## TIPOS DE DATOS ##
####################

# Tipo texto: str
# Tipo numérico: int, float, complex
# Tipo secuencial: list, tuple, range
# Tipo mapeo: dict
# Tipo set: set, frozenset
# Tipo booleano: bool
# Tipo binario: bytes, bytearray, memoryview

# Ejemplos de asignación
x = "Hello World"                             # str   
x = 20                                        # int   
x = 20.5                                      # float   
x = 1j                                        # complex   
x = ["apple", "banana", "cherry"]             # list  
x = ("apple", "banana", "cherry")             # tuple   
x = range(6)                                  # range   
x = {"name" : "John", "age" : 36}             # dict  
x = {"apple", "banana", "cherry"}             # set   
x = frozenset({"apple", "banana", "cherry"})  # frozenset   
x = True                                      # bool  
x = b"Hello"                                  # bytes   
x = bytearray(5)                              # bytearray   
x = memoryview(bytes(5))                      # memoryview