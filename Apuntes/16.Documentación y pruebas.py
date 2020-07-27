################
## DOCSTRINGS ##
################

# En Python todos los objetos cuentan con una variable especial llamada doc
# gracias a la que podemos describir para qué sirven los y cómo se usan los objetos.
# Estas variables reciben el nombre de docstrings, cadenas de documentación.

# Ejemplo
def hola(arg):
    """Este es el docstring de la función"""
    print("Hola", arg, "!")

hola("Héctor")

# Para consultar la documentación hay que utilizar la función reservada help y pasarle el objeto:
help(hola)

# Ejemplo con una clase
class Clase:
    """ Este es el docstring de la clase"""
    def __init__(self):
        """Este es el docstring del inicializador de clase"""
    def metodo(self):
        """Este es el docstring del metodo de clase"""

o = Clase()
help(o)

# Podemos consultar la documentación de un módulo o función:
import requests
help(requests)
help(len)
###########
## PYDOC ##
###########