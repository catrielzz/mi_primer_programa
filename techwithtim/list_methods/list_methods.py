# De forma similar a las cadenas, el tipo de datos de la lista de pitones tiene muchos métodos útiles que podemos
# implementar. Los dos que les voy a mostrar aquí son .count () y .find (). ¡Estos métodos también funcionan en cadenas!

# - .count(): contará cuántas veces aparece un determinado elemento.
# -.find(): encontrará la primera aparición de un artículo y devolverá su índice.

my_list = ["a", "b", "b", "a", "c", "d"]

my_list.count("a")  # -> 2
# my_list.find("a")   # -> 0 Deprecado
my_list.count("b")  # -> 2
# my_list.find("hello")  # -> -1 Deprecado
# Si no se encuentra el elemento .find () devolverá -1

# Problema: nos gustaría verificar la validez de una dirección de correo electrónico. Para nuestros propósitos,
# es válido si contiene una "@", tiene una longitud > = 5 y termina con un ".com"

email = input("Ingrese el Email: ")
if email.count("@") == 1 and len(email) >= 5:
    if email.find(".com") == len(email) - 4:
        print("Email valido.")
    else:
        print("Email invalido")
else:
    print("Email invalido, tiene que contener @ y no tiene que ser mas largo que 5 caracteres")




