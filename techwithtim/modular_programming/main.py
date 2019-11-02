# La programación modular es la práctica de dividir nuestro código en diferentes archivos (módulos) y luego importar
# ese código para que podamos usarlo para muchos proyectos diferentes.
# Por lo general, el código que reutilizará va a su propio módulo, por lo que puede importar ese módulo en lugar de
# copiarlo y pegarlo. Esto hace que nuestros programas sean más legibles, más fáciles de escalar y más agradables
# para trabajar.

# Below is the code contained in two separate python files.

# File name: main.py

from techwithtim.modular_programming import myModule

value = myModule.func(5)  # esto llamará a la función func desde myModule

print(value)  # Esto imprimirá 7


# Podemos usar la palabra clave import para importar módulos que están integrados en python o que hemos creado.
# Nota: Para importar nuestros propios módulos, deben estar en el mismo directorio que el archivo desde
# el que estamos importando.

# Para evitar el uso de "myModule", podemos importar funciones específicas de nuestros módulos utilizando una
# combinación de palabras clave "import" y "from".

from techwithtim.modular_programming.myModule import func

value = func(5)  # ahora solo podemos usar func como una función regular
print(value)  # esto imprime 7


