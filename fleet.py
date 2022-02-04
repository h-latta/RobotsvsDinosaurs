from robot import Robot

class Fleet:

    def __init__(self):
        self.army = []
        self.create_fleet()

    def create_fleet(self):
        robot_one = Robot('Ike')
        robot_two = Robot('Lucy')
        robot_three = Robot('Jim')
        self.army.append(robot_one)
        self.army.append(robot_two)
        self.army.append(robot_three)
