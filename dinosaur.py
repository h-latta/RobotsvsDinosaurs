

class Dinosaur:
    def __init__(self, name, atk_power):
        self.name = name
        self.attack_power = atk_power
        self.health = 50

    def attack(self, robot):
        if robot.health >= 0:
            robot.health = robot.health - self.attack_power
            print(f'{self.name} swiped {robot.name} for {self.attack_power} damage!')
            print(f'{robot.name} is down to {robot.health}HP.')