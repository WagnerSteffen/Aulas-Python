#Herança e polimorfismo

class Mamifero:
    def __init__(self, cor_do_pelo, genero, patas) -> None:
        self.cor_do_pelo = cor_do_pelo
        self.genero = genero
        self.patas = patas
    def falar(self):
        print("Oi, eu sei falar!")
    def andar(self):
        print(f'Estou andando sobre {self.patas} patas')
    def amamentar(self):
        if self.genero.startswith('m'):
            print('Sou macho, nao posso amamentar')
        else:
            print('Estou amamentando')
rex = Mamifero('marrom', 'macho', 4)
rex.falar()
rex.andar()
rex.amamentar()
print()

julia = Mamifero('preta', 'femea', 2)
julia.falar()
julia.andar()
julia.amamentar()
print()

class Pessoa(Mamifero):
    pass


julia = Pessoa('preta', 'femea', 2)
julia.falar()
julia.andar()
julia.amamentar()
print()


class Pessoa(Mamifero):
    def __init__(self, cor_do_pelo, genero, patas, cabelo) -> None:
        super().__init__(cor_do_pelo, genero, patas)
        self.cabelo = cabelo
    def estudar(self):
        print("Estou estudando")
    def falar(self):
        super().falar()
        print("Sou uma pessoa")
        
julia = Pessoa('preta', 'femea', 2, 'loiro')
julia.falar()
print()