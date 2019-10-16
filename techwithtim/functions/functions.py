# La idea básica es que una función es un bloque de código que hace algo. Normalmente usamos funciones cuando repetimos
# la misma tarea o una similar. A continuación se muestra uno de los ejemplos más básicos de una función:


def add_two(x):
    return x + 2


print(add_two(3))  # esto imprimirá 5

# Antes de que podamos profundizar en las funciones, hay algunas definiciones que debemos entender:

# - Parámetros: son la entrada para la función, aparecen entre paréntesis de la definición de la función.
#               En el ejemplo anterior, nuestro único parámetro es x (puede tener tantos parámetros como desee).

# - Argumentos: son lo que nosotros (el programador) pasamos a la función como entrada.
#               Aparecen en la llamada a la función. En el ejemplo anterior, el único argumento es 3.

# Esta función verifica si cada elemento en una lista es cero.
# Nos devuelve un valor Verdadero o Falso dependiendo de la lista dada.


def is_zeros(li):
    for element in li:
        if element != 0:
            return False
    return True


print(is_zeros([0, 0, 0, 1]))  # Esto imprimirá falso

# Esta función verifica si cada elemento en una lista es cero.
# It displays to the screen True or False.
# NO devuelve un valor.


def is_zeros(li):
    check = True
    for element in li:
        if element != 0:
            check = False
            break
    if check:
        print("True")
    else:
        print("False")


is_zeros([0, 0, 0, 0])  # Llamar a esto dará como resultado que True se imprima en la pantalla

# Nota: Las funciones están destinadas a ser reutilizadas y, por lo tanto, se pueden usar tantas veces como desee.
# Si alguna vez se encuentra repitiendo código, piense en ponerlo en una función y
# llamar a esa función en lugar del código repetido.

# Problema: queremos hacer un conjunto de preguntas 5 veces: name, age and country


def ask_questions():
    name = input('Ingrese su Nombre: ')
    age = input('Ingrese su edad: ')
    country = input('Ingrese su pais de residencia: ')
    print('Tu nombre es', name, 'tienes', age, 'vives en', country)


for i in range(5):
    ask_questions()



