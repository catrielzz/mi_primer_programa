# En python tenemos algunas cosas muy útiles llamadas métodos.
# Ahora los métodos son prácticamente cualquier cosa que use en un tipo de datos en el formulario dataType.method ().
# Están integrados en Python y nos ahorran mucho trabajo y mucho tiempo. Python tiene algunos métodos muy útiles que
# podemos usar en la cadena de tipo de datos. Los más utilizados y más útiles son:
# - .strip () eliminará los espacios en blanco al final o al final de una cadena.
# - .split () devolverá una lista de subcadenas de la cadena dada. Por defecto, divide la cadena por espacios
# (cada palabra se convierte en un elemento de la lista). Sin embargo, puede elegir la cadena en la que se dividirá
# insertándola entre corchetes.
# - .lower () hará que cada letra de la cadena sea minúscula.
# - .upper() hará que cada letra de la cadena sea mayúscula.
# - len () * Esto es una función * devolverá la cantidad de caracteres en la cadena dada (incluidos los espacios).

# Ejemplos

my_str = "    my nAME Is YoEl"

my_str.strip()  # -> "my nAME Is YoEl"
my_str.split()  # -> ["my", "nAME", "Is", "YoEl"]
my_str.lower()  # -> "    my name is yoel"
my_str.upper()  # -> "    MY NAME IS YOEL"
print(len(my_str))     # -> 19

# Un ejemplo práctico de cuándo usaríamos estos métodos se puede ver a continuación:
# Queremos que el usuario pueda escribir cualquier variacion de una palabra y que sean correctas.

answer = input("What is my name?:  ")

if answer.lower().strip() == "yoel":
    print("Correct!")
else:
    print("That is incorrect!")




