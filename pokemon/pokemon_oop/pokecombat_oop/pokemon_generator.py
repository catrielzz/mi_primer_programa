from pokemon.pokemon_oop.pokecombat_oop.pokemon_class import Pokemon
import random




class Pikachu(Pokemon):
    pokemon_type = "electric"


class Charmander(Pokemon):
    pokemon_type = "Fire"


class Bulbasaur(Pokemon):
    pokemon_type = "Plant"


class Squirtle(Pokemon):
    pokemon_type = "Water"


def pokemon_choice(pokemon):
    if pokemon == 'PIKACHU':
        pikachu = Pikachu("Pikachu")
        pikachu.stats_generator()
        return pikachu
    elif pokemon == 'CHARMANDER':
        charmander = Charmander("Charmander")
        charmander.stats_generator()
        return charmander
    elif pokemon == 'SQUIRTLE':
        squirtle = Squirtle("Squirtle")
        squirtle.stats_generator()
        return squirtle
    elif pokemon == 'BULBASAUR':
        bulbasaur = Bulbasaur("Bulbasaur")
        bulbasaur.stats_generator()
        return bulbasaur


def random_enemy():
    random_pokemon = random.randrange(0, 3)
    if random_pokemon == 0:
        pikachu = Pikachu("Pikachu")
        pikachu.stats_generator()
        return pikachu
    elif random_pokemon == 1:
        charmander = Charmander("Charmander")
        charmander.stats_generator()
        return charmander
    elif random_pokemon == 2:
        squirtle = Squirtle("Squirtle")
        squirtle.stats_generator()
        return squirtle
    elif random_pokemon == 3:
        bulbasaur = Bulbasaur("Bulbasaur")
        bulbasaur.stats_generator()
        return bulbasaur
