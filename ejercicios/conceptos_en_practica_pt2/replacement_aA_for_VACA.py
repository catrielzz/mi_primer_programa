valores_a_sustituir = ["VACA"]
string_a_cambiar = input("Ingresa una frase: ")

for valor in valores_a_sustituir:
    replacement = string_a_cambiar.replace("A", valor)
    copy = replacement.replace("a", valor)

print(copy)