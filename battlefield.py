from os import name
from fleet import Fleet
from herd import Herd

fleet = Fleet()
herd = Herd()

class Battlefield:
    def __init__(self):
        self.game = self.run_game()
        self.name = name

    def display_welcome(self):
        print('ROBOTS VS DINOSAURS!')
        print("Welcome to the arena. Let's get going!")
        self.name = input("For starters, what's your name? ")
        print(f'Okay {self.name}, get ready to battle!')
    
    def battle(self):
        fleet.create_fleet()
        herd.create_herd()
        print(f'For the robots, we have {fleet.army}.')
        print(f'For the dinosaurs, we have {herd.group}.')

    def dino_turn(self, dinosaur):
        pass

    def robo_turn(self, robot):
        pass

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):
        pass

    def run_game(self):
        Battlefield.display_welcome(self)
        Battlefield.battle(self)

battlefield = Battlefield()

