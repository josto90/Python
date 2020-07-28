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

# Desde la terminal no podemos utilizar la función help, pero sí existe la posibilidad de utilizar pydoc 

### pydoc nombre.py --> Ejecutar en terminal
# Una función interesante de Pydoc es que podemos generar la documentación de nuestro código en HTML utilizando la siguiente sintaxis:

### pydoc -w nombre.py
### pydoc -w .\ --> Genera la documentación de forma recursiva de todo un paquete


#############
## DOCTEST ##
#############

# doctest nos permiten combinar pruebas en la propia documentación.
# Por regla general cada prueba va ligada a una funcionalidad, pueden ser funciones, clases o sus métodos. Por ejemplo:

def suma(a, b):
    """Esta función recibe dos parámetros y devuelve la suma de ambos

    >>> suma(5,10)
    15
    """
    return a+b

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Así únicamente se lanzarán las pruebas al ejecutar directamente el módulo, y ya podremos ejecutar el módulo desde la terminal:

### python test.py -v