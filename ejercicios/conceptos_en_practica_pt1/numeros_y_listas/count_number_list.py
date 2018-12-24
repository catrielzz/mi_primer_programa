numeros = []
largo_de_lista = 0
numeros_para_agregar = ""

while numeros_para_agregar != "FIN":
    numeros_para_agregar = input("Ingresa un numero (Ingresa FIN para terminar): ")
    if numeros_para_agregar != "FIN":
        numeros.append(numeros_para_agregar)

for numero in numeros:
    largo_de_lista += 1

print(numeros)
print("El largo de la lista es: {}".format(largo_de_lista))