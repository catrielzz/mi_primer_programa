import random
pokemon_elegido = input("Contra quien quieres pelear? (Squirtle / Charmander / Bulbasaur): ")
pikachu = "Pikachu"
charmander = (pokemon_elegido == "Charmander")
squirtle = (pokemon_elegido == "Squirtle")
bulbasaur = (pokemon_elegido == "Bulbasaur")



buff = random.randint(0,1)
golpe_normal_charmander = 10
golpe_normal_pikachu = 10
golpe_normal_bulbasaur = 10
golpe_normal_squirtle = 10
golpe_fuego = 12
golpe_agua = 12
golpe_planta = 12
golpe_electrico = 12

if buff == 0:
    print("Charmander uso fortalecer, su ataque se aumento en 2 puntos :" )
    golpe_normal_charmander += 2
    golpe_fuego += 2
elif buff == 1:
    print("Charmander uso , su ataque se aumento en 2 puntos :" )


