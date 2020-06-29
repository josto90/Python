############
## LAMBDA ##
############

# Una función lambda es una pequeña función anónima.
# Una función lambda puede tomar cualquier número de argumentos, pero solo puede tener una expresión.
# Sintaxis: lambda argumentos : expresión

x = lambda a : a + 10
print(x(5)) 

print()
# Varios argumentos:
x = lambda a, b : a * b
print(x(5, 6)) 

print()

# Ejemplo de su potencial. 
def myfunc(n):
  return lambda a : a * n 

mydoubler = myfunc(2) # Devuelve lambda a : a * 2 
print(mydoubler(11))

print()

mytripler = myfunc(3)
print(mytripler(11))