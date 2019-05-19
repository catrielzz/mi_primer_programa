import random


class Periferico:

    def __init__(self, alto, ancho, peso, profundidad, color):
        self.numero_serie = random.randrange(100, 10000)
        self.estado = 100
        self.alto = alto
        self.ancho = ancho
        self.peso = peso
        self.profundidad = profundidad
        self.color = color


class Monitor(Periferico):
    pulgadas = int
    conectores = list
    botones = list
    resolucion = list


class Teclado(Periferico):
    numero_teclas = int
    idioma = str

