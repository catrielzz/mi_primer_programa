import goslate

salida = False
agenda = dict()

while not salida:
    pregunta = input("Que quieres hacer? [Anadir numero[A] / Consultar numero[C] / Salir[S]]:").upper()

    # Anadir numero
    if pregunta == 'A':
        print("Vamos a anadir un numero de telefono: ")
        print("--------------------------------------")
        nombre = input("Ingrese el nombre: ")
        numero = input("Ingrese el numero: ")
        agenda[nombre] = numero

    # Consultar numero
    elif pregunta == 'C':
        print("Consultar numero: ")
        print("--------------------------------------")
        nombre = input("De quien quieres saber el numero: ")
        print(agenda[nombre])

    # Salir del programa
    elif pregunta == 'S':
        salida = True