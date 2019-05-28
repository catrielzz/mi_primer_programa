def numero_mas_grande_entre_tres(primero, segundo, tercero):
    mas_grande = primero
    if segundo > mas_grande:
        mas_grande = segundo
    if tercero > primero:
        mas_grande = tercero
    return mas_grande

print(numero_mas_grande_entre_tres(4, 7, 5))
