import random
from weapon import Weapon

sword = Weapon('Sword', 15)
dino_blaster = Weapon('Dino Blaster', 25)
club = Weapon('Club', 10)

weapon_list = [sword, dino_blaster, club]

random_weapon = random.choice(weapon_list)

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = random_weapon

    def attack(self, dinosaur):
        if dinosaur.health > 0:
            dinosaur.health = dinosaur.health - (self.weapon.attack_power)
            print(f'{self.name} used their {self.weapon.name} on {dinosaur.name} for {self.weapon.attack_power} damage!')
        else:
            pass