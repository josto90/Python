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


