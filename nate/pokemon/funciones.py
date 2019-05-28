import random

# Vida pokemones
vida_pikachu = 100
vida_enemigo = 0

def ataque_normal(pikachu, pokemon_elegido):
    golpe_normal_pokemon_elegido = 10
    golpe_normal_pikachu = 10
    golpe_especial = 12
    ataque_random = random.randint(0, 2)
    accuracy_golpe_normal_pikachu = random.randint(0, 1)
    accuracy_golpe_normal_pokemon_elegido = random.randint(0, 1)
    accuracy_golpe_fuego = random.randint(0, 1)
    buff = random.randint(0, 1)

    if accuracy_golpe_normal_pikachu == 0:
        pokemon_elegido -= golpe_normal_pikachu
        print(pikachu, " uso golpe normal, la vida de ", pokemon_elegido, " es: ", vida_enemigo)
        if ataque_random == 0:
            if accuracy_golpe_normal_pokemon_elegido == 0:
                pikachu -= golpe_normal_pokemon_elegido
                print(pokemon_elegido, " uso Golpe normal por ", golpe_normal_pokemon_elegido,
                      " la vida de pikachu es: ",
                      pikachu)
            elif accuracy_golpe_normal_pokemon_elegido == 1:
                print(pokemon_elegido, " fallo su ataque..")
        elif ataque_random == 1:
            if accuracy_golpe_fuego == 0:
                pikachu -= golpe_especial
                print(pokemon_elegido, " uso Golpe normal por ", golpe_especial, " la vida de pikachu es: ",
                      pikachu)
            elif accuracy_golpe_fuego == 1:
                print(pokemon_elegido, " fallo su ataque..")
        elif ataque_random == 2:
            if buff == 0:
                print(pokemon_elegido, " uso fortalecer, su ataque se aumento en 2 puntos :")
                golpe_normal_pokemon_elegido += 2
                golpe_especial += 2
            elif buff == 1:
                print(pokemon_elegido, " uso defensa, los ataques de Pikachu son mas debiles")
                golpe_normal_pikachu -= 2
    elif accuracy_golpe_normal_pikachu == 1:
        print("Has fallado el ataque")
        if ataque_random == 0:
            if accuracy_golpe_normal_pokemon_elegido == 0:
                pikachu -= golpe_normal_pokemon_elegido
                print(pokemon_elegido, " uso Golpe normal por ", golpe_normal_pokemon_elegido,
                      " la vida de pikachu es: ",
                      pikachu)
            elif accuracy_golpe_normal_pokemon_elegido == 1:
                print(pokemon_elegido, " fallo su ataque..")
        elif ataque_random == 1:
            if accuracy_golpe_fuego == 0:
                pikachu -= golpe_especial
                print(pokemon_elegido, " uso Golpe normal por ", golpe_especial, " la vida de pikachu es: ",
                      vida_pikachu)
            elif accuracy_golpe_fuego == 1:
                print(pokemon_elegido, " fallo su ataque..")
        elif ataque_random == 2:
            if buff == 0:
                print(pokemon_elegido, " uso fortalecer, su ataque se aumento en 2 puntos :")
                golpe_normal_pokemon_elegido += 2
                golpe_especial += 2
            elif buff == 1:
                print(pokemon_elegido, " uso defensa, los ataques de Pikachu son mas debiles")
                golpe_normal_pikachu -= 2

