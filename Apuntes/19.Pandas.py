############
## PANDAS ##
############

## SERIES

# Series es una matriz unidimensional con etiquetas capaz de contener datos de cualquier tipo 
# (entero, cadena, flotante, objetos de python, etc.). 
# Las etiquetas del eje se denominan colectivamente índice.

import pandas as pd
s = pd.Series([3,5,7])
print(s)

print()

asignaturas = ['matematicas','historia','fisica','literatura']
notas = [8,6,9,7]
serie_notas = pd.Series(notas, index=asignaturas)
print(serie_notas)

print(serie_notas['fisica'])
print(serie_notas[serie_notas >=8])

print()

# Sele pueden asignar nombres

serie_notas.name = 'Notas'
serie_notas.index.name = 'Índice de notas'

print(serie_notas)

print()

# Se puede convertir a diccionario

diccionario = serie_notas.to_dict()
print(diccionario)

# DATAFRAMES

import pandas as pd
import webbrowser
website = 'https://es.wikipedia.org/wiki/Anexo:Campeones_de_la_NBA'
webbrowser.open(website)

dataframe_nba = pd.read_clipboard() # Recupera información del portapapeles. Hay que copiar primero los datos al portapapeles
print(dataframe_nba)

print(dataframe_nba.columns) # Vemos los nombres de las columnas
print(dataframe_nba['Campeón del Oeste ']) # Seleccionamos esta columna

print(dataframe_nba.head()) # Muestra los 5 primeros
print(dataframe_nba.tail()) # Muestra los 5 últimos


# Creamos un dataframe a partir de un diccionario

asignaturas = ['matematicas','historia','fisica']
notas = [7,8,9]
diccionario = {'Asignaturas':asignaturas, 'Notas':notas}
dataframe_notas = pd.DataFrame(diccionario)
print(dataframe_notas)

print()


# INDICES
import pandas as pd

valores = [1,2,3]
indices = ['a','b','c']
serie = pd.Series(valores, index=indices)
print(serie.index[0])
# serie.index[0] = 'z' --> Da error, ya que los índices no son mutables

valores = [[6,7,8],[8,9,5],[6,9,7]]
indices = ['matematicas','historia','fisica']
nombres = ['Antonio','Pedro','María']

dataframe = pd.DataFrame(valores,index=indices,columns=nombres)
print(dataframe)

print()

# Eliminar elementos
valores = [1,2,3]
indices = ['a','b','c']
serie = pd.Series(valores, index=indices)
print(serie)
serie = serie.drop('c')
print(serie)

# Operaciones en series y dataframes
import pandas as pd
import numpy as np

serie1 = pd.Series([0,1,2], index=['a','b','c'])
serie2 = pd.Series([3,4,5,6], index=['a','b','c','d'])

print(serie1 + serie2)
print()

valores = np.arange(4).reshape(2,2)
indices = list('ab')
columnas = list('12')

dataframe = pd.DataFrame(valores,index=indices, columns=columnas)

valores2 = np.arange(9).reshape(3,3)
indices2 = list('abc')
columnas2 = list('123')
dataframe2 = pd.DataFrame(valores2,index=indices2, columns=columnas2)

print(dataframe + dataframe2)

# Estadisticas
print(dataframe.describe())
print(dataframe.max()) # Hay muchas opciones

# Unión de dataframes
import pandas as pd
dataframe1 = pd.DataFrame({'c1':['1','2','3'], 'clave':['a','b','c']})
dataframe2 = pd.DataFrame({'c2':['4','5','6'], 'clave':['c','b','e']})

dataframe3 = pd.DataFrame.merge(dataframe1,dataframe2)
print(dataframe3)






