# El operador "slice" es exclusivo de python y hace que nuestras vidas como programadores sean MUCHO más fáciles.
# Es algo una combinación entre la función de rango y la indexación. Puede pensar en un segmento como una sección
# (o parte) o una colección.

# El operador slice tiene argumentos opcionales para si decide dejar las cosas en blanco.
# Comenzará automáticamente en el índice 0, se detendrá al final y pasará por 1 a menos que declare lo contrario.
# Aquí hay algunos ejemplos del operador slice en uso.

my_str = "hello"

my_str[1:]   # -> "ello"
my_str[:3]   # -> "hel" (we don't include the stopping point)
my_str[::2]  # -> "hlo"
"new string to slice"[4:12:2]  # -> "srn "

# El operador slice también es útil para insertar elementos en una lista en un índice determinado.
# Esta funcionalidad específica solo está disponible para listas.

# my_list = [97, 98, 99, 100]
#
# my_list[1:1] = 40
#
# print(my_list)  # prints [97, -40, 98, 99, 100] does not work

# La indexación negativa funciona de manera similar a la indexación positiva donde -1 representa el último elemento
# de la lista y -len (lista) representa el primer elemento. También podemos usar indexación negativa para segmentar

fruits = ["apple", "pear", "banana"]

fruits[-1]  # -> "banana"
fruits[-3]  # -> "apple"

fruits[-2:]   # -> ["pear", "banana"]
fruits[::-1]  # -> ["banana","pear","apple"]
# Doing [::-1] reverses the list

# These same properties apply to strings and tuples

my_str = "hello"
my_str[-1]    # -> "o"
my_str[::-1]  # -> "olleh"
my_str[:-3]   # -> "he"





