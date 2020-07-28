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

# Acceso a elementos
print('Segundo elemento de la primera dimensión: ', arr2[0, 1])

print()

# Muestra del array
print(arr3[1:5]) 

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
