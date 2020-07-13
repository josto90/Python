################
## ITERADORES ##
################

# Un iterador es un objeto que contiene un número contable de valores.
# Un iterador es un objeto sobre el que se puede iterar, lo que significa que puede atravesar todos los valores.
# Técnicamente, en Python, un iterador es un objeto que implementa el protocolo de iterador, que consiste en los métodos __iter__() y __next__().

# Iterador vs Iterable
# Las listas, tuplas, diccionarios y conjuntos son todos objetos iterables. Son contenedores iterables de los que puede obtener un iterador.
# Todos estos objetos tienen un método iter() que se utiliza para obtener un iterador:

tupla = ("manzana", "plátano", "cereza")
myit = iter(tupla)

print(next(myit))
print(next(myit))
print(next(myit))

# Crear un iterador
# Para crear un objeto/clase como iterador, debe implementar los métodos __iter__() y __next__() en su objeto.
# El método __iter__() actúa de manera similar a __init__(), puede realizar operaciones (inicializar, etc.), pero siempre debe devolver el objeto iterador.
# El método __next__() también le permite realizar operaciones y debe devolver el siguiente elemento de la secuencia.

class MisNumeros:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

miClase = MisNumeros()
miIter = iter(miClase)

print(next(miIter))
print(next(miIter))
print(next(miIter))
print(next(miIter))
print(next(miIter)) 