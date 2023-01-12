"""
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer.
Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor
que 21 anos, ela deve crescer 0,5 cm.
"""
class person(object):
    def __init__(self, name: str, age: int, weight: int, hight: float) -> None:
        """
        Generetes a "person"

        Args:
            name (str): the name of the person
            age (int): the age in years
            weight (int): weight in kg
            hight (int): hight in cm
        """
        self.name = name
        self.age = age
        self.weight = weight
        self.hight = hight
        print(f"{self.name} was successfully created")

        
    def older(self, time:int) -> None:
        """
        Make the person older
        For each year that the person grows older, she/he will grow 0,5cm as well.

        Args:
            time (int): the amount of time in years that will add to the age
        """
        for year in range(1, time+1):
            if self.age < 21:
                self.hight += 0.5
            self.age += year
        print(f"Now I'm {self.age} years old")
        
    def feed(self, amount: int) -> None:
        """
        Add the amount in weight

        Args:
            amount (int): the weight in kg that the person will gain
        """
        self.weight += amount
        print(f"Now my weight is: {self.weight} kg")
    
    def grow(self, hight: int) -> None:
        """
        Make the person taller

        Args:
            hight (int): the amout of centimeter that the person will grow
        """
        self.hight += hight
        print(f"Now my hight is: {self.hight} centimeters")
    
    def says_hi(self) -> None:
        print(f"""\nHi! My name is {self.name} and I'm {self.age} years old.\nMy hight is: {self.hight}\nMy weight is: {self.weight}\n""")


#Showoff
wagner = person("Wagner", 29, 72, 179)
wagner.says_hi()
wagner.older(2)
wagner.feed(2)
wagner.grow(10)
wagner.says_hi()

    
        