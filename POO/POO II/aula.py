class Pessoa(object):

    def __init__(self, name, weight, dog) -> None:
        self.name = name
        self.weight = weight
        self.dog = dog
        
    def train(self) -> None:
        self.dog.pawn()
        self.dog.bark()

class dogs(object):
    def __init__(self, name, color) -> None:
        self.name = name
        self.color = color
    
    def pawn(self) -> None:
        print(f"{self.name} give the pawn")
    
    def bark(self) -> None:
        print("auauauauauauauauauauau!")

codi = dogs("Codi", "brown")
wagner = Pessoa("Wagner", 72, codi)
wagner.dog.bark()
wagner.train()
wagner.dog.pawn()