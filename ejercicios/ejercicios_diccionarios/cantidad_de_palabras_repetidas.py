diccionario = dict()

frase = input("Ingresa una frase: ")

for palabra in frase:
    if palabra in diccionario:
        diccionario[palabra] += 1
        print()
    else:
        diccionario[palabra] = 1

if palabra >=1:
    print("{} 1 vez".format(palabra))
else:
    print("{} {} veces".format(palabra, len(palabra)))
