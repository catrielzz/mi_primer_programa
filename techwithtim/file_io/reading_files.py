# En muchos casos, es posible que deseemos utilizar información almacenada en archivos. Python hace que sea muy fácil
# para nosotros abrir y leer archivos de texto y analizarlos en una lista para su posterior procesamiento.

# * IMPORTANTE * Antes de intentar abrir un archivo de texto existente, asegúrese de que esté en el mismo directorio
# que su script de Python. ¡Esto simplemente significa que siempre que su archivo de Python esté almacenado en su
# computadora, su archivo de texto debe estar allí con él! Por ejemplo, si su archivo Python está almacenado en su
# Escritorio en la carpeta Python, entonces su archivo de texto debe estar también en esa carpeta Python.
# O puede indicar donde se encuentra su archivo con comandos de bash ej: ../carpeta/archivo.txt

# Esta es la sintaxis básica para abrir un archivo:
f = open("file.txt", "r")

# La función abierta toma dos argumentos. El primero es el nombre del archivo ("file.txt") y el segundo es el modo ("r")
# El modo le dirá a Python si está leyendo, escribiendo o agregando al documento. En nuestro caso usamos "r" para leer.
# Una vez que hemos abierto el archivo y lo hemos almacenado en una variable (en nuestro caso f), podemos usar el método
# .readlines () para convertir cada línea en un elemento en una lista.

lines = f.readlines()  # lines se parece a ["línea 1 \ n", "línea 2 \ n", "línea 3"]

# Ahora puede notar que cada elemento en la lista (excluyendo el último en algunos casos) tiene un "\ n" final.
# Este "\ n" se conoce como un carácter de escape y así es como los programas saben que deben ir a una nueva línea.
# Por lo general, este carácter no es visible para nosotros, pero como estamos leyendo el contenido del archivo,
#  lo vemos. Para eliminar este carácter, podemos utilizar el método .strip ().

lines = f.strip().readlines()  # lines se parece a ["línea 1", "línea 2", "línea 3"]






