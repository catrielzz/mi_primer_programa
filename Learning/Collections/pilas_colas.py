# Una pila es una coleccion de elementos ordenados:
#   - LIFO(Last in First out) o en español, ultimo en entrar primero en salir.

pila = [3, 4, 5]

for i in range(6, 9):
    pila.append(i)
print(pila)

pila.pop()  # Elimina el ultimo elemento de la lista si no se le pasa ningun valor
for item in range(len(pila)):
    print(pila)
    pila.pop()

# Una cola es una coleccion donde el primer elmento en entrar es el primero en salir
#   - FIFO(First in First out) Primero en entrar, primero en salir

from collections import deque

cola = deque([])



