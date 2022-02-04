from os import name
from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd
import random
from robot import Robot


class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        self.game = self.run_game()
        self.name = name

    def display_welcome(self):
        print('ROBOTS VS DINOSAURS!')
        print("Welcome to the arena. Let's get going!")
        self.name = input("For starters, what's your name? ")
        print(f'Okay {self.name}, get ready to battle!')
        print(f'For the robots, we have {self.fleet.army[0].name, self.fleet.army[1].name, self.fleet.army[2].name}.')
        print(f'For the dinosaurs, we have {self.herd.group[0].name, self.herd.group[1].name, self.herd.group[2].name}.')
        input("You ready to fight? ")
    
    def battle(self):
        self.dino_turn()
        self.show_robo_opponent_options()
        self.robo_turn()
        self.show_dino_opponent_options()

    def dino_turn(self):
        print("Okay, it's time for the dinosaurs to attack!")
        print("Robots, brace yourselves!")
        random_robot = random.choice(self.fleet.army)
        dino_atk = random.choice(self.herd.group)
        attack_damage = Dinosaur.attack(dino_atk, random_robot)

    def show_dino_opponent_options(self):
        print(f'{self.herd.group[0].name} has {self.herd.group[0].health}HP left.')
        print(f'{self.herd.group[1].name} has {self.herd.group[1].health}HP left.')
        print(f'{self.herd.group[2].name} has {self.herd.group[2].health}HP left.')
        confirm = input('Continue? (press any key) ')
    
    def robo_turn(self):
        print("Now it's time for the robots to attack!")
        robot_atk = random.choice(self.fleet.army)
        random_dino = random.choice(self.herd.group)
        damage_dealt = Robot.attack(robot_atk, random_dino)

    def show_robo_opponent_options(self):
        print(f'{self.fleet.army[0].name} has {self.fleet.army[0].health}HP left.')
        print(f'{self.fleet.army[1].name} has {self.fleet.army[1].health}HP left.')
        print(f'{self.fleet.army[2].name} has {self.fleet.army[2].health}HP left.')
        confirm = input('Continue? (press any key) ')

    def display_winners(self):
        finish_game = False
        while finish_game == False:
            if self.herd.group[0].health <= 0 and self.herd.group[1].health <= 0 and self.herd.group[2].health <= 0:
                finish_game == True
                print("Well done! You defeated the dinosaurs!")
                break
            elif self.fleet.army[0].health <= 0 and self.fleet.army[1].health <= 0 and self.fleet.army[2].health <= 0:
                finish_game == True
                print("The dinosaurs were too strong! We'll get them next time.")
                break
            else:
                Battlefield.battle(self)

    def run_game(self):
        Battlefield.display_welcome(self)
        Battlefield.battle(self)
        Battlefield.display_winners(self)

