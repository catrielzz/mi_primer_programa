diccionario_de_colores = {"ROJO": "red!",
                          "AMARILLO": "yellow!",
                          "VERDE": "green!",
                          "AZUL": "blue!"}
salir = False
while not salir:
    pregunta = input("Que quieres hacer? [Consultar color[C] / Salir[S]]: ").upper()
    if pregunta != 'C' and pregunta != 'S':
        print("Opcion incorrecta...")
    # Juego de color
    elif pregunta == 'C':
        color_usuario = input("Ingrese el color a traducir: ").upper()
        while color_usuario not in diccionario_de_colores:
            color_usuario = input("Por favor, ingrese un color valido [rojo, amarillo, verde, azul]: ").upper()
        print(diccionario_de_colores[color_usuario])
    elif pregunta == 'S':
        salir = True