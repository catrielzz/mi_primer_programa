nombres_y_fechas = dict()
salir = False

while not salir:
    pregunta = input("Que quieres hacer? [Agregar datos[A] / Consultar datos[C] / Salir[S]]: ").upper()

    # Agregar datos
    if pregunta == 'A':
        print("Vamos a agregar las fechas de nacimiento: ")
        print("-------------------------------------------")
        nombre = input("Ingrese un nombre: ").upper()
        fecha_de_nacimiento = input("Ingrese fecha de nacimiento: ")
        nombres_y_fechas[nombre] = fecha_de_nacimiento

    # Consultar datos
    elif pregunta == 'C':
        print("Vamos a consultar los datos: ")
        print("-------------------------------------------")
        nombre = input("De quien quieres saber la fecha de nacimiento: ").upper()
        print(nombres_y_fechas[nombre])

    # Salir
    elif pregunta == 'S':
        salir = True