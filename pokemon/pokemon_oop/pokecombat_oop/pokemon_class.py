import random
from time import sleep


class Pokemon:
    base_hp = None
    base_attack = None
    pokemon_name = None
    pokemon_type = None

    def __init__(self, name):
        self.hp = self.base_hp
        self.pokemon_name = name

    def attack(self, enemy):
        coin_flip = random.randrange(0, 20)
        if (coin_flip <= 10 and enemy.base_hp > 0) and self.base_hp > 0:
            enemy.take_damage(self.base_attack)
            print("{} ha hecho {} de daño".format(self.pokemon_name, self.base_attack))
            if enemy.base_hp >= 0:
                enemy.show_hp()
            else:
                print("{} ya no puede continuar el ganador es {}".format(enemy.pokemon_name, self.pokemon_name))

            sleep(1)
        elif coin_flip >= 10:
            print("{} fallo el ataque..".format(self.pokemon_name))
            sleep(1)

    def take_damage(self, damage):
        self.base_hp -= damage

    def show_stats(self):
        print("Has elegido a {}\nvida: {}\ndaño: {}".format(self.pokemon_name, self.base_hp, self.base_attack))

    def show_hp(self):
        print("La vida de {} es: {}".format(self.pokemon_name, self.base_hp))

    def stats_generator(self):
        self.base_hp = random.randrange(90, 130)
        self.base_attack = random.randrange(9.0, 13.0)

