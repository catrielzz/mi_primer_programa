quieres_helado_input = input("Quieres un helado? (Si/No): ").upper()

if quieres_helado_input == "SI":
    quieres_helado = True
elif quieres_helado_input == "NO":
    quieres_helado = False
else:
    print("Respuesta incorrecta, lo tomo como un no.. ")
    quieres_helado = False



tienes_dinero_input = input("Tienes dinero para un helado? (Si/No): ").upper()
esta_el_vendedor_input = input("Esta el vendedor? (Si/No): ").upper()
estas_con_tu_tia_input = input("Estas con tu tia?? (Si/No): ").upper()
estas_con_tu_tia = "SI"
tienes_dinero = "SI"
puedes_comprarlo = tienes_dinero or estas_con_tu_tia
esta_el_vendedor =  esta_el_vendedor_input == "SI"

if quieres_helado  and puedes_comprarlo and esta_el_vendedor:
    print("Comer helado")
else:
    print("Pues nada")