def devolver_pares(lista_de_numeros):
    lista_pares = []
    for numero in lista_de_numeros:
        if numero % 2 == 0:
            lista_pares.append(numero)
    return lista_pares

print(devolver_pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))