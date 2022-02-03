from os import name
from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd
import random

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
        input("You ready to fight? ")

    def dino_turn(self):
        print("Okay, it's time for the dinosaurs to attack!")
        print("Robots, brace yourselves!")

    def robo_turn(self):
        print("Now it's time for the robots to attack!")
        print(f'Attack! -{random.choice(fleet.army)}')

    def show_dino_opponent_options(self):
        random_dino = (random.choice(fleet.army)
        dino_atk = herd.dino_base.attack_power


    def show_robo_opponent_options(self):
        robo_choice = input(f'Who do you want to select this turn? {fleet.army}')
        if robo_choice == fleet.army:
            dino_choice = input(f'Now who do you want to attack? {herd.group}')
            if dino_choice == herd.group:
                attack = fleet.robot.weapon.attack_power
                

    def display_winners(self):
        finish_game = False
        while finish_game == False:
            if herd.group == []:
                finish_game == True
                print("Well done! You defeated the dinosaurs!")
            elif fleet.army == []:
                finish_game == True
                print("The dinosaurs were too strong! We'll get them next time.")
            else:
                Battlefield.dino_turn(self)
                Battlefield.show_dino_opponent_options(self)
                Battlefield.robo_turn(self)
                Battlefield.show_robo_opponent_options(self)
                Battlefield.display_winners(self)

    def run_game(self):
        Battlefield.display_welcome(self)
        Battlefield.battle(self)
        Battlefield.dino_turn(self)
        Battlefield.show_dino_opponent_options(self)
        Battlefield.robo_turn(self)
        Battlefield.show_robo_opponent_options(self)
        Battlefield.display_winners(self)

