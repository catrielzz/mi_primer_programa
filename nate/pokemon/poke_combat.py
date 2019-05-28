pokemon_elegido = input("Contra quien quieres pelear? (Squirtle / Charmander / Bulbasaur): ").upper()
vida_pikachu = 100
vida_enemigo = 0

if pokemon_elegido == "SQUIRTLE":
    nombre_pokemon = "Squirtle"
    vida_enemigo = 90
    ataque_pokemon = 9

elif pokemon_elegido == "CHARMANDER":
    nombre_pokemon = "Charmander"
    vida_enemigo = 80
    ataque_pokemon = 8

elif pokemon_elegido == "BULBASAUR":
    nombre_pokemon = "Bulbasaur"
    vida_enemigo = 100
    ataque_pokemon = 10


while vida_pikachu > 0 and vida_enemigo > 0:
    #Elegimos el ataque
    ataque_elegido = input("Que ataque quieres usar? (Sparkle / Thunderbolt): ").upper()
    pikachu = "Pikachu"
    #Si el ataque elegido es sparkle entonces hacemos 10 de dano, sino si el ataque es thunderbolt hacemos 12 de dano,
    #sino pasamos el turno
    if ataque_elegido == "SPARKLE":
        vida_enemigo -= 10
        ataque_elegido = "Sparkle por 10 de dano"

    elif ataque_elegido == "THUNDERBOLT":
        vida_enemigo -= 12
        ataque_elegido = "Thunderbolt por 12 de dano"
    else:
        ataque_elegido = "Has pasado de turno"

    vida_pikachu -= ataque_pokemon

    print("{} ha usado {}, la vida de {} ahora es {}".format(pikachu, ataque_elegido, nombre_pokemon, vida_enemigo))
    print("{} te ha hecho {} de dano, la vida de {} ahora es {}".format(nombre_pokemon, ataque_pokemon, pikachu, vida_pikachu))

if vida_enemigo <= 0:
    print("Has ganado!")
elif vida_pikachu <= 0:
    print("Has perdido!")

print("Combate terminado")