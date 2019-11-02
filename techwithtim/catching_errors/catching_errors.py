# n python podemos exceptuar ciertos errores y evitar que nuestro programa falle.
# Para hacer esto, usamos una declaración try and except.

# Un error común con el que podrías toparte es intentar convertir una cadena en un int

print("I will add 5 to any number you give me.")
num = input("type a number:")

addedNum = int(num) + 5
print("5 +", num, "is", addedNum)  # ValueError: invalid literal for int() with base 10: 'asd'

# No podemos convertir la cadena "hola" en un número entero, por lo tanto, recibimos un error.
# Para corregir este error, podemos usar una declaración try and except.
# El programa intentará realizar cualquier operación dentro de la declaración de prueba.
# Si por algún motivo se produce un error, en lugar de bloquear el programa, dejará la instrucción try y hará lo que
# esté dentro de la instrucción except.

print("I will add 5 to any number you give me.")
num = input("type a number:")

try:
    addedNum = int(num) + 5
    print("5 +", num, "is", addedNum)
except ValueError:
    print("That is not a number!!")
