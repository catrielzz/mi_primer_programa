lista_mixta = [1, 2, "tres", "cuatro", 5, "seis"]
lista_strings = []
lista_ints = []

for elemento in lista_mixta:
    if type(elemento) == str:
        lista_strings.append(elemento)
    else:
        lista_ints.append(elemento)

print(lista_strings)
print(lista_ints)
