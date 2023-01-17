pessoa = {'nome':'Wagner', 'idade': 29, 'cor_dos_olhos': 'castanho'}
print(pessoa['nome'])

class Pessoa:
    pass

wagner = Pessoa()
wagner.nome = 'Wagner'
wagner.idade = 20
wagner.cor_dos_olhos = 'castanho'
print(wagner.__dict__)

dic = dict(nome = 'Wagner', idade = 20, cor_dos_olhos = 'castanho')
print(dic)

class Pessoa:
    def __init__(self, nome, idade, cor_dos_olhos) -> None:
        self.nome = nome
        self.idade = idade
        self.cor_dos_olhos = cor_dos_olhos
    def ola():
        print(f'Oi, meu nome é {self.nome} e eu tenho {self.idade} anos!')
wagner = Pessoa('Wagner', 20, 'castanho')
print("\n",wagner.__dict__, "\n")
print(Pessoa.__dict__, "\n")

#Python is a slow language, there is a way to make it faster. Programming closer to C#.