from robot import Robot

robot_one = Robot('Ike')
robot_two = Robot('Lucy')
robot_three = Robot('Jim')

class Fleet:
    def __init__(self):
        self.army = []

    def create_fleet(self):
        robo_list = [robot_one.name, robot_two.name, robot_three.name]
        self.army = robo_list
