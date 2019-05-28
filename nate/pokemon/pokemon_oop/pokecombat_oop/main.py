from time import sleep

from nate.pokemon.pokemon_oop.pokecombat_oop.pokemon_generator import *


def main():
    fight_round = 1
    pokemon_choiced = input("Elige tu pokemon inicial!! (Squirtle / Charmander / Bulbasaur / Pikachu): ").upper()
    my_pokemon = pokemon_choice(pokemon_choiced)
    my_pokemon.show_stats()
    sleep(2)
    enemy_pokemon = random_enemy()
    enemy_pokemon.show_stats()
    sleep(2)

    while my_pokemon.base_hp > 0 and enemy_pokemon.base_hp > 0:
        print("round {}".format(fight_round))
        my_pokemon.attack(enemy_pokemon)
        print("-------------------------")
        enemy_pokemon.attack(my_pokemon)
        print("-------------------------")
        fight_round += 1
        sleep(2)


if __name__ == "__main__":
    main()
