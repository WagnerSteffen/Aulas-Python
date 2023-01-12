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
class retangle(object):
    def __init__(self, h:int, l:int, vertex) -> None:
        """
        Create a retangle with hight 'h' and side 'l'

        Args:
            h (int): the hight of the retangle
            l (int): the side of the retangle
            vertex (object): the starting point of the retangle
        """
        self.hight = h
        self.side = l
        print("Retangle created with success!")
        
    def plot(self) -> None:
        self.vertex.posicion()
        print(f"""
The posicion of the retangle is:
x, y: {self.vertex.x},{self.vertex.y}
x',y: {self.vertex.x + self.side},{self.vertex.y}
x,y': {self.vertex.x},{self.vertex.y + self.hight}
x',y': {self.vertex.x + self.side}, {self.vertex.y + self.hight}
""")
        
    def center(self) -> None:
        x_center = self.vertex.y + self.hight
        y_center = self.vertex.x + self.side
        print(f'The center of the retangle is x: {x_center} and y:{y_center}')
        
class dot(object):
    def __init__(self, x = 0, y = 0) -> None:
        """
        Create a dot in cartesian space

        Args:
            x (int): where in axis x
            y (int): where in axis y
        """
        self.x = x
        self.y = y
        print("The dot was selected!")
    
    def posicion(self) -> None:
        print(f"The posicion x,y of the vertex is: {self.x},{self.y}")
    
def main():
    print("Choose your option: ")
    op = 0
    while op != 5:
        op = int(input("1 - Create/change a retangle\n2 - Create/change a vertex\n3 - Print the center of the retangle\n4 - Print all information\n5 - Exit\nSelect: "))
        if op == 1:
            h = int(input("What is the hight of the retangle? "))
            l = int(input("What is the side of the retangle? "))
            create_vertex = bool(input("Do you wish to create the vertex now? 1 - yes | 0 - No\n:"))
            
            if create_vertex:
                x = int(input("Where in axis x? "))
                y = int(input("Where in axis y? "))
                vertex = dot(x,y)
            else:
                vertex = dot()

            rtg = retangle(h,l,vertex)    
        elif op == 2:
            x = int(input("Where in axis x? "))
            y = int(input("Where in axis y? "))
            vertex = dot(x, y)
        elif op == 3:
            rtg.center()
        elif op == 4:
            rtg.plot()
        elif op == 5:
            exit()
        else:
            op = int(input("Select one of the options above: "))

main()