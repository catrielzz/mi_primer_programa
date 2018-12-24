numero_tabla = int(input("De que numero quieres la tabla de multiplicar: "))

for multiplo in range(5,16):
    if (numero_tabla * multiplo) % 2 == 0:
        print("{} x {} = {}".format(numero_tabla, multiplo, numero_tabla * multiplo))
