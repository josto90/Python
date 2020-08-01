###########
## NUMPY ##
###########

# NumPy es una biblioteca de Python utilizada para trabajar con matrices.
# También tiene funciones para trabajar con álgebra lineal.

# En Python tenemos listas que sirven al propósito de las matrices, pero su procesamiento es lento. NumPy proporciona un objeto de matriz 50 veces más rápido.
# El objeto de matriz en NumPy se llama ndarray, proporciona muchas funciones de soporte que hacen que trabajar con ndarray sea muy fácil.
import numpy as np
arr = np.array([1, 2, 3, 4, 5]) # También se puede con ((1,2,3,4,5))
print(arr)
print(type(arr))

print()

# Arrays multidimensionales

arr0 = np.array(15) # 0D
print(arr0)
print()

arr1 = np.array([1, 2, 3, 4, 5]) # 1D
print(arr1)
print()

arr2 = np.array([[1, 2, 3], [4, 5, 6]]) # 2D
print(arr2)
print()

arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]) # 3D
print(arr3)
print()

# Comprobar el número de dimensiones
print(arr0.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim) 

print()


# Generando arrays

arr0 = np.zeros(4)
print(arr0)

print()

arr0 = np.ones(4)
print(arr0)

print()

arr0 = np.arange(4)
print(arr0)

print()

arr0 = np.arange(2,20,3) # inicio, fin, salto
print(arr0)

print()

lista1 = [1,2,3,4]
arr0 = np.array(lista1)
print(arr0)

print()


# Operaciones con arrays

import numpy as np
array1 = np.array([1,2,3,4])

array1 = array1 + 4 # Le suma 4 a cada elemento
print(array1)

array1 = array1 / 2
print(array1)

print()

# Indexación arrays
import numpy as np
array = np.arange(0,11)
print(array)
print(array[0:3])

print()

# Muestra del array
print(array[1:5]) 

print()

# Acceso a elementos concretos
print('Segundo elemento de la primera dimensión: ', arr2[0, 1]) # Array definido mas arriba bidimensional

print()

# Mtrices traspuestas(cambio de filas por columnas)
import numpy as np
array = np.arange(15).reshape((3,5)) # 3 filas, 5 columnas
print(array)

array_tras = array.T
print(array_tras)

# Entrada y salida arrays
import numpy as np
array1 = np.arange(6)

np.save('array1s',array1) # Salvamos el array de manera física
np.load('array1s.npy')

np.savetxt('mificheroaaray.txt',array1,delimiter=',')
np.loadtxt('mificheroaaray.txt',delimiter=',')

# Funciones con arrays
import numpy as np
array1 = np.arange(5)
array2 = np.arange(5)

print(np.sqrt(array1)) # Raíz cuadrada

print(np.random.rand(5)) # Números random

print(np.add(array1,array2)) # Suma de dos arrays
