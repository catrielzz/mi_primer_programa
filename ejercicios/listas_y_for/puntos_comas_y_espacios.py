frase_introducida = input("Introduce una frase completa: ")

puntos = ["."]
comas = [","]
espacios = [" "]

n_puntos = 0
n_comas = 0
n_espacios = 0

for char in frase_introducida:
    if char in puntos:
        n_puntos += 1
    elif char in comas:
        n_comas += 1
    elif char in espacios:
        n_espacios += 1

print("puntos = {}".format(n_puntos))
print("comas = {}".format(n_comas))
print("espacios = {}".format(n_espacios))
