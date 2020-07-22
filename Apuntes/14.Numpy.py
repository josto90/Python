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