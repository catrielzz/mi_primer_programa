operaciones = input("Que operacion quieres hacer? (Multiplicar / Dividir / Restar / Sumar): ").upper()

numero_a = int(input("Ingrese el primer numero: "))
numero_b = int(input("Ingrese el segundo numero: "))

if operaciones == "MULTIPLICAR":
    nombre_operacion = "multiplicado por "
    valor_de_operacion = numero_a * numero_b

if operaciones == "DIVIDIR":
    nombre_operacion = "dividido por "
    valor_de_operacion = numero_a / numero_b

if operaciones == "RESTAR":
    nombre_operacion = "menos "
    valor_de_operacion = numero_a - numero_b

if operaciones == "SUMAR":
    nombre_operacion = "mas "
    valor_de_operacion = (numero_a + numero_b)

print("El numero {} {} {} es igual a {}".format(numero_a, nombre_operacion, numero_b, valor_de_operacion))