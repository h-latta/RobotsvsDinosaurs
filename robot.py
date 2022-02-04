from weapon import Weapon

sword = Weapon('Sword', 15)

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = sword

    def attack(self, dinosaur):
        if dinosaur.health >= 0:
            dinosaur.health = dinosaur.health - self.weapon.attack_power
            print(f'{self.name} swiped {dinosaur.name} for {self.weapon.attack_power} damage!')
            print(f'{dinosaur.name} is down to {dinosaur.health}HP.')