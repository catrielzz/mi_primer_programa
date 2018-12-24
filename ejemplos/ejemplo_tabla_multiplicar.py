numero_tabla = int(input("De que numero quieres la tabla de multiplicar: "))

for multiplo in range(0,11):
    print("{} x {} = {}".format(numero_tabla, multiplo, numero_tabla * multiplo))
