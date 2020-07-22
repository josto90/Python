##############
## FICHEROS ##
##############

# La función clave para trabajar con archivos en Python es la función open(). Toma dos parámetros: nombre de archivo y modo.
# Existen cuatro modos diferentes para abrir un archivo:

# "r" - Leer - Valor predeterminado. Abre un archivo para leer, error si el archivo no existe
# "a" - Agregar - Abre un archivo para agregar, crea el archivo si no existe
# "w" - Escribir - Abre un archivo para escribir, crea el archivo si no existe
# "x" - Crear - Crea el archivo especificado, devuelve un error si el archivo existe

# Además, puede especificar si el archivo debe manejarse en modo binario o de texto

# "t" - Texto - Valor predeterminado. Modo de texto
# "b" - Binario - Modo binario (por ejemplo, imágenes)

f = open("demofile.txt", "rt") # rt son valores por defecto. No es necesario especificarlos.
