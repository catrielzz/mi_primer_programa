# try:
#     n = float(input('Introduce un numero: '))
#     m = 4
#     print('{}/{}={}'.format(n, m, n / m))
# except ValueError:
#     print('Ha ocurrido un error, por favor introduce un numero valido')


# while True:
#     try:
#         n = float(input('Introduce un numero: '))
#         m = 4
#         print('{}/{}={}'.format(n, m, n / m))
#         break  # Importante romper la ejecucion despues de que sea un resultado valido.
#     except ValueError:
#         print('Ha ocurrido un error, por favor introduce un numero valido')


# while True:
#     try:
#         n = float(input('Introduce un numero: '))
#         m = 4
#         print('{}/{}={}'.format(n, m, n / m))
#     except ValueError:
#         print('Ha ocurrido un error, por favor introduce un numero valido')
#     else:
#         print('Todo ha funcionado correctamente.')
#         break # Importante romper la ejecucion despues de que sea un resultado valido.


while True:
    try:
        n = float(input('Introduce un numero: '))
        m = 4
        print('{}/{}={}'.format(n, m, n / m))
    except ValueError:
        print('Ha ocurrido un error, por favor introduce un numero valido')
    else:
        print('Todo ha funcionado correctamente.')
        break # Importante romper la ejecucion despues de que sea un resultado valido.
    finally:
        print('Fin de la iteracion.')


# ----------------------------------------------------------------------------------------------------------------------
# Multiples Excepciones

try:
    n = input('ingrese un numero')
    5/n
except Exception as e:
    print(type(e).__name__)





