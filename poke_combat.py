pokemon_elegido = input("Contra quien quieres pelear? (Squirtle / Charmander / Bulbasaur): ").upper()
vida_pikachu = 100
vida_enemigo = 0

charmander = (pokemon_elegido == "CHARMANDER")
squirtle = (pokemon_elegido == "SQUIRTLE")
bulbasaur = (pokemon_elegido == "BULBASAUR")

if charmander or squirtle or bulbasaur:
    if squirtle:
        vida_enemigo = 90
        print("La vida de Squirtle es : ",vida_enemigo)
        while vida_pikachu > 0 and vida_enemigo > 0:
            ataque_elegido = input("Que ataque quieres usar? (Sparkle / Thunderbolt): ").upper()
            if ataque_elegido == "SPARKLE":
                vida_enemigo -= 10
                vida_pikachu -= 8
                print("La vida de Squirtle es : ", vida_enemigo)
                print("La vida de Pikachu es : ", vida_pikachu)
            elif ataque_elegido == "THUNDERBOLT":
                vida_enemigo -= 12
                vida_pikachu -= 8
                print("La vida de Squirtle es : ", vida_enemigo)
                print("La vida de Pikachu es : ", vida_pikachu)
            else:
                print("Has pasado de ronda")
                vida_pikachu -= 8
                print("La vida de Squirtle es : ", vida_enemigo)
                print("La vida de Pikachu es : ", vida_pikachu)
    if charmander:
        vida_enemigo = 80
        print(vida_enemigo)

    if bulbasaur:
        vida_enemigo = 100
        print(vida_enemigo)

else:
    print("Ingrese un pokemon valido")