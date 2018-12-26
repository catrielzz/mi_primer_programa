lista_numeros = [1, 10, 70, 30, 50, 55]
multiplos_de_2 = []
multiplos_de_3 = []
multiplos_de_5 = []
multiplos_de_7 = []

for numero in lista_numeros:
    if lista_numeros[numero] % 2 == 0 or lista_numeros[numero] % 3 == 0 or lista_numeros[numero] % 5 == 0 or\
            lista_numeros[numero] % 7 == 0:
        valor_a_agregar = 0
        if numero % 2 == 0:
            valor_a_agregar += lista_numeros[numero]
            multiplos_de_2.append(valor_a_agregar)
        elif numero % 3 == 0:
            valor_a_agregar += lista_numeros[numero]
            multiplos_de_3.append(valor_a_agregar)
        elif numero % 5 == 0:
            valor_a_agregar += lista_numeros[numero]
            multiplos_de_5.append(valor_a_agregar)
        elif numero % 7 == 0:
            valor_a_agregar += lista_numeros[numero]
            multiplos_de_7.append(valor_a_agregar)

print("Multiplos_2 = {}".format(multiplos_de_2))
print("Multiplos_3 = {}".format(multiplos_de_3))
print("Multiplos_5 = {}".format(multiplos_de_5))
print("Multiplos_7 = {}".format(multiplos_de_7))
