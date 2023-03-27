#Abstração, Atributo/Métodos Estáticos e Encapsulamento

#Abstração
class ObjetoGrafico(object):
    def __init__(self, cor) -> None:
        self.cor = cor
    def area(self):
        pass
    def perimetro(self):
        pass
    def info(self):
        print(f"Serão preenchidos {self.area()} metros quadrados com a cor: {self.cor}")