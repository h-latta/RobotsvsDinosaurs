from weapon import Weapon

sword = Weapon('Sword', 10)

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = sword