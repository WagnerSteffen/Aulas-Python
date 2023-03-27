"""
Defina uma nova classe ObjetoGráfico subclasse de object, cujos atributos são:
    cor_de_preenximento --> inteiro
    preenchida --> bool
    cor_de_contorno --> inteiro

Escreva três classes:
    Retangulo --> Atributos: base e altura
    Circulo --> Atributos: raio
    Triangulo --> Atributos: base e altura

Subclasses da classe ObjetoGráfico que possuam todas métodos area e perimetro  
"""
class ObjetoGrafico(object):
    def __init__(self, cor_de_preenchimento:int, preenchida:bool, cor_de_contorno:int) -> None:
        self.cor_de_preenchimento = cor_de_preenchimento
        self.preenchida = preenchida
        self.cor_de_contorno = cor_de_contorno


class Retangulo(ObjetoGrafico):
    def __init__(self, cor_de_preenchimento: int, preenchida: bool, cor_de_contorno: int, base:int, altura:int) -> None:
        super().__init__(cor_de_preenchimento, preenchida, cor_de_contorno)
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura
    def perimetro(self):
        return self.base + self.altura

class Circulo(ObjetoGrafico):
    def __init__(self, cor_de_preenchimento: int, preenchida: bool, cor_de_contorno: int, raio:int) -> None:
        super().__init__(cor_de_preenchimento, preenchida, cor_de_contorno)
        self.raio = raio
    def area(self):
        return 3.14 * self.raio**2
    def perimetro(self):
        return 2*3.14*self.raio
    
class Triangulo(ObjetoGrafico):
    def __init__(self, cor_de_preenchimento: int, preenchida: bool, cor_de_contorno: int, base:int, altura: int) -> None:
        super().__init__(cor_de_preenchimento, preenchida, cor_de_contorno)
        self.base = base
        self.altura = altura
    def area(self):
        return (self.base*self.altura)/2
    def perimetro(self):
        pass
triangulo = Triangulo(1, 1, 1, 2, 3)
print(triangulo.area())
print()
circulo = Circulo(1,1,1,4)
print(circulo.area())
print()
retangulo = Retangulo(1,1,1,5,4)
print(retangulo.area())
print()

