from dinosaur import Dinosaur

dino_one = Dinosaur('Grog', 20)
dino_two = Dinosaur('Rex', 15)
dino_three = Dinosaur('Spike', 10)

class Herd:
    def __init__(self):
        self.group = []

    def create_herd(self):
        dino_list = [dino_one.name, dino_two.name, dino_three.name]
        self.group = dino_list
