from dinosaur import Dinosaur

class Herd:

    def __init__(self):
        self.group = []
        self.create_herd()

    def create_herd(self):
        dino_one = Dinosaur('Grog', 20)
        dino_two = Dinosaur('Lex', 20)
        dino_three = Dinosaur('Spike', 20)
        self.group.append(dino_one)
        self.group.append(dino_two)
        self.group.append(dino_three)
