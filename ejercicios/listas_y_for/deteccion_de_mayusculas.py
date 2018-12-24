frase = input("Ingrese una frase: ")

mayuscula = "abcdefghijklmnopqrstuvwxyz".upper()

n_mayuscula = 0
for letra in frase:
    if letra in mayuscula:
        n_mayuscula += 1

print("Cantidad de mayusculas en la frase: {}".format(n_mayuscula))
