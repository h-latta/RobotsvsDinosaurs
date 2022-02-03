from weapon import Weapon

weapon = Weapon()

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = weapon('Sword', 10)