from dinosaur import Dinosaur

dino_base = Dinosaur('', 20)
dino_one = Dinosaur('Grog', 20)
dino_two = Dinosaur('Lex', 20)
dino_three = Dinosaur('Spike', 20)

class Herd:
    dino_base = Dinosaur('', 20)
    
    def __init__(self):
        self.group = []
        self.roster = [dino_one, dino_two, dino_three]

    def create_herd(self):
        dino_list = [dino_one.name, dino_two.name, dino_three.name]
        self.group = dino_list
