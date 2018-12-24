frase = input("Introduce una frase: ")

vocales = ["a","e","i","o","u"]

lista_de_vocales = []

for char in frase:
    if char in vocales:
        lista_de_vocales.append(char)
print(lista_de_vocales)