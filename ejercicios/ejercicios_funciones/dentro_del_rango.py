def dentro_del_rango(numero, minimo, maximo):
    if numero >= minimo and numero <= maximo:
        return True
    else:
        return False

print(dentro_del_rango(25, 1, 100))
