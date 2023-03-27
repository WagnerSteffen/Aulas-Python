"""
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""

class Quadrado(object):
    def __init__(self, lado:int) -> None:
        self.lado = lado
        
    def muda_lado(self, size) -> None:
        self.lado = size
        print(f"Lado do quadrado alterado para {self.lado}")
        
    def retorna_lado(self) -> None:
        print(f"O lado do quadrado é {self.lado}")
    
    def area(self) -> None:
        print(self.lado*self.lado)
        
square = Quadrado(5)
square.retorna_lado()
square.muda_lado(4)
square.area()