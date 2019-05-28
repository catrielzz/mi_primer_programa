myString = input("Ingresa una frase: ")
result = ''
counter = 1

for valor in range(len(myString)):
    if myString[valor] == 'a' or myString[valor] == 'e' or myString[valor] == 'i' or myString[valor] == 'o' \
            or myString[valor] == 'u':
        result += str(counter)
        counter += 1
    else:
        result += myString[valor]
print(result)