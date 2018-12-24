numeros = []
largo_de_lista = 0
numeros_para_agregar = 0
numero = 0

while numeros_para_agregar != "FIN":
    numeros_para_agregar = input("Ingresa un numero (Ingresa FIN para terminar): ")
    if numeros_para_agregar != "FIN":
        numeros.append(int(numeros_para_agregar))

for valor_elemento in numeros:
    numero += valor_elemento
for cantidad in numeros:
    largo_de_lista += 1

promedio = numero / largo_de_lista
print("Los valores de la lista son: {}".format(numeros))
print("El largo de la lista es: {}".format(largo_de_lista))
print("EL promedio de la suma de los valores de los elementos de la lista es: {}".format(promedio))