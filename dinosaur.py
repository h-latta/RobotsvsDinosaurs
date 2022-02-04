

import random


class Dinosaur:
    def __init__(self, name, atk_power):
        self.name = name
        self.attack_power = atk_power
        self.health = 50

    def attack(self, robot):
        attack_names = ['bit', 'swiped', 'clawed', 'slashed']
        if robot.health > 0:
            robot.health = robot.health - self.attack_power
            print(f'{self.name} {random.choice(attack_names)} {robot.name} for {self.attack_power} damage!')
        else:
            pass