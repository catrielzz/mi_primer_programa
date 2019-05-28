"""
Crea un programa que cuente el número de veces que aparece una palabra en una string

"Hola Hola como estas amigo amigo amigo"
-----------------
|  Hola: 2 veces |
|  como: 1 vez   |
|  estas: 1 vez  |
|  amigo: 3 veces|
-----------------
"""
frase = input('Ingrese una frase: ')
def contador_palabras(str):
    diccionario = dict()
    palabras = str.split()

    for palabra in palabras:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1

    return diccionario

print(contador_palabras(frase))




