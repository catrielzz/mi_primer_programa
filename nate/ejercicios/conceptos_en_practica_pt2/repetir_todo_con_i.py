valores_a_sustituir = ["i"]
string_a_cambiar = input("Ingresa una frase: ")

for valor in valores_a_sustituir:
    replacement = string_a_cambiar.replace("a", valor)
    replacement = replacement.replace("e", valor)
    replacement = replacement.replace("o", valor)
    replacement = replacement.replace("u", valor)


print(replacement)