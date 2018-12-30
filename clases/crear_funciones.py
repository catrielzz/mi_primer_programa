mi_lista = [2, 3, 4, 5]


def largo(lista):
    largo = 0
    for item in lista:
        largo += 1

    return largo


print(largo(mi_lista))

def input_con_confirmacion(pregunta_usuario):
    confirmado = False
    while not confirmado:
        dato_usuario = input(pregunta_usuario)
        confirmacion = input("Has dicho {}, estas seguro? (Si/No): ".format(dato_usuario)).upper()
        if confirmacion == "SI":
            confirmado = True
    return dato_usuario

pregunte = input_con_confirmacion("Cual es tu nombre: ")



def reverse_string(string_to_reverse):
    reversed_string = ""
    current_index = len(string_to_reverse) - 1
    while current_index >= 0:
        reversed_string += string_to_reverse[current_index]
        current_index -= 1
    return reversed_string

print(reverse_string("Hola"))