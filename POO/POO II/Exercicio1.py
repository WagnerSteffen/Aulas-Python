"""
Classe Ponto e Retangulo:
Faça um programa completo utilizando funções e classes que:

#Possua uma classe chamada Ponto, com os atributos x e y.
#Possua uma classe chamada Retangulo, com os atributos largura e altura.
#Possua uma função para imprimir os valores da classe Ponto
Possua uma função para encontrar o centro de um Retângulo.
Você deve criar alguns objetos da classe Retangulo.
Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior
esquerdo do retângulo, que deve ser um objeto da classe Ponto.

A função para encontrar o centro do retângulo deve retornar o valor para um
objeto do tipo ponto que indique os valores de x e y para o centro do objeto.

O valor do centro do objeto deve ser mostrado na tela

Crie um menu para alterar os valores do retângulo e imprimir o centro deste
retângulo.
"""

class Ponto:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y
    def imprime(self):
        print(f'O ponto é x:{self.x}, y:{self.y}')

class Retangulo:
    def __init__(self, b = 0, h = 0, vertice = Ponto()) -> None:
        self.b = b 
        self.h = h
        self.vertice = vertice
    def centro(self):
        x = self.vertice.x + self.b/2
        y = self.vertice.y + self.h/2
        return Ponto(x,y)

def main():
    ret = Retangulo()
    while True:
        comando = menu()
        if comando.startswith('m'):
            ret.h = float(input("Digite a altura(h) do retangulo: "))
            ret.b = float(input("Digite a base(b) do retangulo: "))
            ret.vertice.x = float(input("Digite o ponto em X do vertice: "))
            ret.vertice.y = float(input("Digite o ponto em Y do vertice: "))
        elif comando.startswith('i'):
            ret.centro().imprime()
        else:
            break
        
def menu():
    while True:
        operacao = str(input("Deseja MUDAR(m), IMPRIMIR(i) ou FECHAR(f)?\n:"))
        operacao.lower()
        if not operacao.isalpha():
            print('Digite apenas letras')
        elif operacao.startswith(('i','m','f')):
            return operacao
        else:
            print('Problemas em interpretar a entrada!')
main()