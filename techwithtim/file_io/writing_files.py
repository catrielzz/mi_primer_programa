# Escribir en un archivo es extremadamente similar a leer. La única diferencia es el modo en que abrimos el archivo.
# Hay dos modos de escritura que podemos usar, agregar y escribir.

# Agregar a un archivo se agregará al final del mismo. Si abrimos en un archivo en modo "a",
# debemos asegurarnos de que esté en el mismo directorio que nuestro script de Python.

f = open("file.txt", "a")

# Abrir un archivo en "w" o en modo de escritura borrará el archivo completo si existe.
#  Si no existe, creará uno nuevo para nosotros.

f = open("file.txt", "w")

# Una vez que hayamos abierto nuestro archivo, podemos escribirle cosas.
# Si nos gustaría escribir en una nueva línea cada vez, debemos asegurarnos de incluir un "\ n"
# al final de nuestra declaración de escritura.

f = open("file.txt", "w")

lines = ["line 1", "line 2", "line 3"]
for line in lines:
    f.write(line + "\n")

f.close()  # Una vez que hayamos terminado de escribir, debemos cerrar el archivo para guardar los cambios.





