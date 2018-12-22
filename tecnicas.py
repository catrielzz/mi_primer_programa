import random

# pokemones
pokemon_elegido = input("Contra quien quieres pelear? (Squirtle / Charmander / Bulbasaur): ")
pikachu = "Pikachu"
charmander = (pokemon_elegido == "Charmander")
squirtle = (pokemon_elegido == "Squirtle")
bulbasaur = (pokemon_elegido == "Bulbasaur")

# Vidas
vida_enemigo = 0
vida_pikachu = 100

# Acciones
buff = random.randint(0, 1)
golpe_normal_charmander = 10
golpe_normal_pikachu = 10
golpe_normal_bulbasaur = 10
golpe_normal_squirtle = 10
golpe_fuego = 12
golpe_agua = 12
golpe_planta = 12
golpe_electrico = 12
accuracy = random.randint(0, 1)

ataque_random = random.randint(0, 2)

if charmander or squirtle or bulbasaur:
    if charmander:
        vida_enemigo = 90
        print("La vida de Charmander es : ", vida_enemigo)
        while vida_pikachu > 0 and vida_enemigo > 0:
            ataque_elegido = input("Que accion quieres usar? (Golpe Normal / Golpe Electrico / Buff random): ").upper()
            if ataque_elegido == "GOLPE NORMAL":
                if accuracy == 0:
                    vida_enemigo -= golpe_normal_pikachu
                    if ataque_random == 0:
                        if accuracy == 0:
                            vida_pikachu -= golpe_normal_charmander
                            print("Charmander uso Golpe normal por ", golpe_normal_charmander,
                                  " la vida de pikachu es: ",
                                  vida_pikachu)
                    elif ataque_random == 1:
                        if accuracy == 0:
                            vida_pikachu -= golpe_fuego
                            print("Charmander uso Golpe normal por ", golpe_fuego, " la vida de pikachu es: ",
                                  vida_pikachu)
                    elif ataque_random == 2:
                        if buff == 0:
                            print("Charmander uso fortalecer, su ataque se aumento en 2 puntos :")
                            golpe_normal_charmander += 2
                            golpe_fuego += 2
                        elif buff == 1:
                            print("Charmander uso defensa, los ataques de ", pokemon_elegido, " son mas debiles")
                            golpe_agua -= 2
                            golpe_electrico -= 2
                            golpe_planta -= 2
                            golpe_normal_bulbasaur -= 2
                            golpe_normal_pikachu -= 2
                            golpe_normal_squirtle -= 2
                elif accuracy == 1:
                    print("Has fallado el ataque")
                    if ataque_random == 0:
                        if accuracy == 0:
                            vida_pikachu -= golpe_normal_charmander
                            print("Charmander uso Golpe normal por ", golpe_normal_charmander,
                                  " la vida de pikachu es: ",
                                  vida_pikachu)
                    elif ataque_random == 1:
                        if accuracy == 0:
                            vida_pikachu -= golpe_fuego
                            print("Charmander uso Golpe normal por ", golpe_fuego, " la vida de pikachu es: ",
                                  vida_pikachu)
                    elif ataque_random == 2:
                        if buff == 0:
                            print("Charmander uso fortalecer, su ataque se aumento en 2 puntos :")
                            golpe_normal_charmander += 2
                            golpe_fuego += 2
                        elif buff == 1:
                            print("Charmander uso defensa, los ataques de ", pokemon_elegido, " son mas debiles")
                            golpe_agua -= 2
                            golpe_electrico -= 2
                            golpe_planta -= 2
                            golpe_normal_bulbasaur -= 2
                            golpe_normal_pikachu -= 2
                            golpe_normal_squirtle -= 2
            elif ataque_elegido == "GOLPE ELECTRICO":
                if accuracy == 0:
                    vida_enemigo -= golpe_electrico
                    if ataque_random == 0:
                        if accuracy == 0:
                            vida_pikachu -= golpe_normal_charmander
                            print("Charmander uso Golpe normal por ", golpe_normal_charmander,
                                  " la vida de pikachu es: ",
                                  vida_pikachu)
                    elif ataque_random == 1:
                        if accuracy == 0:
                            vida_pikachu -= golpe_fuego
                            print("Charmander uso Golpe normal por ", golpe_fuego, " la vida de pikachu es: ",
                                  vida_pikachu)
                    elif ataque_random == 2:
                        if buff == 0:
                            print("Charmander uso fortalecer, su ataque se aumento en 2 puntos :")
                            golpe_normal_charmander += 2
                            golpe_fuego += 2
                        elif buff == 1:
                            print("Charmander uso defensa, los ataques de ", pokemon_elegido, " son mas debiles")
                            golpe_agua -= 2
                            golpe_electrico -= 2
                            golpe_planta -= 2
                            golpe_normal_bulbasaur -= 2
                            golpe_normal_pikachu -= 2
                            golpe_normal_squirtle -= 2
                elif accuracy == 1:
                    print("Has fallado el ataque")
                    if ataque_random == 0:
                        if accuracy == 0:
                            vida_pikachu -= golpe_normal_charmander
                            print("Charmander uso Golpe normal por ", golpe_normal_charmander,
                                  " la vida de pikachu es: ",
                                  vida_pikachu)
                    elif ataque_random == 1:
                        if accuracy == 0:
                            vida_pikachu -= golpe_fuego
                            print("Charmander uso Golpe normal por ", golpe_fuego, " la vida de pikachu es: ",
                                  vida_pikachu)
                    elif ataque_random == 2:
                        if buff == 0:
                            print("Charmander uso fortalecer, su ataque se aumento en 2 puntos :")
                            golpe_normal_charmander += 2
                            golpe_fuego += 2
                        elif buff == 1:
                            print("Charmander uso defensa, los ataques de ", pokemon_elegido, " son mas debiles")
                            golpe_agua -= 2
                            golpe_electrico -= 2
                            golpe_planta -= 2
                            golpe_normal_bulbasaur -= 2
                            golpe_normal_pikachu -= 2
                            golpe_normal_squirtle -= 2
            elif ataque_elegido == "BUFF RANDOM":
                if buff == 0:
                    print("Pikachu uso fortalecer, su ataque se aumento en 2 puntos :")
                    golpe_normal_pikachu += 2
                    golpe_electrico += 2
                elif buff == 1:
                    print("Pikachu uso defensa, los ataques de ", pokemon_elegido, " son mas debiles")
                    golpe_agua -= 2
                    golpe_fuego -= 2
                    golpe_planta -= 2
                    golpe_normal_bulbasaur -= 2
                    golpe_normal_charmander -= 2
                    golpe_normal_squirtle -= 2
                if ataque_random == 0:
                    vida_pikachu -= golpe_normal_charmander
                    print("Charmander uso Golpe normal por ", golpe_normal_charmander, " la vida de Pikachu es: ",
                          vida_pikachu)
                elif ataque_random == 1:
                    vida_pikachu -= golpe_fuego
                    print("Charmander uso Golpe normal por ", golpe_fuego, " la vida de pikachu es: ",
                          vida_pikachu)
                elif ataque_random == 2:
                    if buff == 0:
                        print("Charmander uso fortalecer, su ataque se aumento en 2 puntos :")
                        golpe_normal_charmander += 2
                        golpe_fuego += 2
                    elif buff == 1:
                        print("Charmander uso defensa, los ataques de Pikachu son mas debiles")
                        golpe_agua -= 2
                        golpe_electrico -= 2
                        golpe_planta -= 2
                        golpe_normal_bulbasaur -= 2
                        golpe_normal_pikachu -= 2
                        golpe_normal_squirtle -= 2
            else:
                print("Has pasado de ronda")

    # if charmander:
    #     vida_enemigo = 80
    #     print(vida_enemigo)
    #
    # if bulbasaur:
    #     vida_enemigo = 100
    #     print(vida_enemigo)

else:
    print("Ingrese un pokemon valido")
