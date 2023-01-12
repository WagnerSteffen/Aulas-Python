#Criando objeto
class Meu_Objeto(object):
    #Metodo construtor
    def __init__(self) -> None:
        self.nome = "Wagner"
        self.idade = 29
        print("Construtor chamado com sucesso")
    #Criando função
    def imprime(self):
        print(f"Ola meu nome é {self.nome} e eu tenho {self.idade}")
        
wagner = Meu_Objeto()

print(wagner.imprime())