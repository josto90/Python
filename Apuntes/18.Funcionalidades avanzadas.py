#################
## GENERADORAS ##
#################

# Por regla general las funciones devolvuelven un valor con return, 
# pero la preculiaridad de los generadores es que van cediendo valores sobre la marcha, 
# en tiempo de ejecución.

def pares(n):
    for numero in range(n+1):
        if numero % 2 == 0:
            yield numero # la función generadora utiliza el yield, que significa ceder.
 
for numero in pares(10):
    print(numero)

print()

# la función integrada next() nos permite acceder al siguiente elemento de la secuencia.
# Se asemeja al funcionamiento de un puntero en la lectura de un fichero

pares = pares(3)
print(next(pares))
print(next(pares))

# no podemos iterar ninguna colección como si fuera una secuencia. 
# Sin embargo, hay una función muy interesante que nos permite covertir las cadenas 
# y algunas colecciones a iteradores, la función iter():

lista = [1,2,3,4,5]
lista_iterable = iter(lista)
print( next(lista_iterable) )
print( next(lista_iterable) )
print( next(lista_iterable) )
print( next(lista_iterable) )
print( next(lista_iterable) )


##########################
## COMPRESION DE LISTAS ##
##########################

# Método tradicional
lista = []
for letra in 'casa':
    lista.append(letra)
print(lista)

# Con comprensión de listas
lista = [letra for letra in 'casa']
print(lista)


############
## FILTER ##
############

# A partir de una lista o iterador y una función condicional, 
# es capaz de devolver una nueva colección con los elementos filtrados que cumplan la condición.

def multiple(numero):    # Primero declaramos una función condicional
    if numero % 5 == 0:  # Comprobamos si un numero es múltiple de cinco
        return True      # Sólo devolvemos True si lo es

numeros = [2, 5, 10, 23, 50, 33]

print(list(filter(multiple, numeros))) # Hay que hacerle un cast a list para almacenar los elementos devueltos

#########
## MAP ##
#########

# Aplica una función sobre todos los elementos y como resultado se devuelve un iterable de tipo map

def doblar(numero):
    return numero*2

numeros = [2, 5, 10, 23, 50, 33]

print(list(map(doblar, numeros)))