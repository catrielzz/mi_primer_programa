
numero_inicial = 10

while numero_inicial > 0:
    if numero_inicial % 2 == 0:
        print(numero_inicial, " es par")
    else:
        print(numero_inicial, " es impar")
    numero_inicial -= 1

print("Finished!")