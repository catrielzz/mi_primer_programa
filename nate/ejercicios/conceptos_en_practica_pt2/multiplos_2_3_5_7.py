lista_numeros = [1, 10, 70, 30, 50, 55]
multiplos_de_2 = []
multiplos_de_3 = []
multiplos_de_5 = []
multiplos_de_7 = []

for numero in lista_numeros:
    if numero % 2 == 0:
        multiplos_de_2.append(numero)
    if numero % 3 == 0:
        multiplos_de_3.append(numero)
    if numero % 5 == 0:
        multiplos_de_5.append(numero)
    if numero % 7 == 0:
        multiplos_de_7.append(numero)


print("Multiplos_2 = {}".format(multiplos_de_2))
print("Multiplos_3 = {}".format(multiplos_de_3))
print("Multiplos_5 = {}".format(multiplos_de_5))
print("Multiplos_7 = {}".format(multiplos_de_7))
