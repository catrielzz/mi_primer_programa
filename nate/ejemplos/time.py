from time import sleep
import datetime

NIGHT_STARTS = 19
DAY_STARTS = 7
HOUR_DURATION = 1


'''
Funcion para escribir en archivo y imprimir por pantalla,
abrimos un archivo, escribimos texto, e imprimimos por pantalla el texto
'''


def write_file_and_screen(text, file_name):
    with open(file_name, 'a') as hours_file:
        hours_file.write("{}{}".format(text, "\n"))
        print(text)


def main():
    """
    Creaamos variable current_time con el tiempo actual, inicializamos variable is_night en falso, creamos
    un bucle infinito, adentro del bucle creamos un sleep que tome como tiempo la constante HOUR_DURATION
    a la variable current time le agregamos el valor de HOUR_DURATION hora, inicializamos la variable
    light_changed en false,
    --Primer condicional--
    si (current time es mayor o igual a NIGHT_STARTS o menor a DAY_STARTS) y no es de noche:
        es de noche y la luz cambio,
    sino si (current_time es mayor o igual a DAY_STARTS y menor que NIGHT_STARTS) y ademas es is_night:
        no es de noche y la luz cambio.
    --Segundo condicional--
    si light_changed:
        si is_night:
            usar funcion write_file_and_screen("Se ha hecho de noche", "horas.txt")
        sino:
            usar funcion write_file_and_screen("Se ha hecho de dia", "horas.txt")

    usar funcion write_file_and_screen("La hora actual es: {}".format(current_time), "horas.txt")
    """
    current_time = datetime.datetime.now()
    is_night = False

    while True:
        sleep(HOUR_DURATION)
        current_time += datetime.timedelta(hours=HOUR_DURATION)
        light_changed = False

        if (current_time.hour >= NIGHT_STARTS or current_time.hour < DAY_STARTS) and not is_night:
            is_night = True
            light_changed = True
        elif DAY_STARTS <= current_time.hour < NIGHT_STARTS and is_night:
            is_night = False
            light_changed = True

        if light_changed:
            if is_night:
                write_file_and_screen("Se ha hecho de noche", "horas.txt")
            else:
                write_file_and_screen("Se ha hecho de dia", "horas.txt")

        write_file_and_screen("La hora actual es: {}".format(current_time), "horas.txt")


if __name__ == "__main__":
    main()
