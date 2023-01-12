"""
Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e
calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe
as medidades de um local. Depois, deve criar um objeto com as medidas e calcular
a quantidade de pisos necessárias para o local.
"""
class retangle(object):
    def __init__(self, h:int, l:int) -> None:
        """
        Create a retangle

        Args:
            h (int): the hight of the retangle
            l (int): the side of the retangle
        """
        self.hight = h
        self.side = l
        print(f"The retangle({self.hight},{self.side}) was successfully created")
        
    def change_side(self) -> None:
        """
        Change the hight to side and side to hight
        """
        print(f"Old hight: {self.hight}, old side: {self.side}")
        self.hight, self.side = self.side, self.hight
        print(f"New high: {self.hight}, new side: {self.side}")
        
    def return_value(self) -> int:
        """
        Return the value of hight and side
        """
        print(f"""The hight is: {self.hight}, the side is: {self.side}""")
        return self.hight, self.side
    
    def area(self) -> None:
        """
        Calculate the area of the retangle
        """
        print(f"The area is: {self.hight * self.side} square meters")
    
    def perimeter(self) -> None:
        """
        Calculate the perimeter of the retangle
        """
        print(f"The perimeter is: {self.hight + self.side} meters")
 
    
#Show off
retangulo = retangle(5,4)
retangulo.change_side()
retangulo.return_value()
retangulo.area()
retangulo.perimeter()
    
        