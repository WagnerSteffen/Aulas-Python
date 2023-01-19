"""
Escreva um programa de bancos que possua:
    Uma classe Banco com os atributos
    - private total
    - public TaxaReserva
    - private reservaExigida

    E métodos
    - public podeFazerEmprestimo(valor) --> bool
    - public MudaTotal(valor)

E uma classe conta com os atributos
    - private saldo
    - private ID
    - private senha

    E métodos
    - public deposito(senha, valor)
    - public saque(senha, valor)
    - public podeReceberEmprestimo(valor) --> bool
    - public saldo --> float
"""
class Banco(object):
    """
    _summary_

    Args:
        object (_type_): _description_

    Returns:
        _type_: _description_
    """
    __total = 1000
    taxaReserva = 0.1
    __reservaExigida = __total*taxaReserva
    def __init__(self, banco) -> None:
        self.banco = banco

    def podeFazerEmprestimo(self, valor) -> bool:
        if valor < Banco.__reservaExigida:
            Banco.__total -= valor
            print("O emprestimo pode ser feito")
            return True
        else:
            print("Nao pode receber emprestimo")
            return False
        
    def status(self) -> None:
        print(Banco.__total)

class Conta(Banco):
    """
    _summary_

    Args:
        Banco (_type_): _description_
    """
    def __init__(self, banco, conta, senha, saldo = 0) -> None:
        super().__init__(banco)
        self.__saldo = saldo
        self.__conta = conta
        self.__senha = senha

    def deposito(self, senha, valor) -> None:
        if self.__senha == senha:
            self.__saldo += valor
        else:
            print("Senha invalida")
    def saque(self,senha, valor) -> None:
        if self.__senha == senha:
            self.__saldo -= valor
        else:
            print("Senha invalida")
    def podeReceberEmprestimo(self, valor):
        if podeFazer := Banco.podeFazerEmprestimo(self, valor = valor):
            self.__saldo += valor
        
    def saldo(self, conta, senha) -> float:
        if self.__conta == conta and self.__senha == senha:
            print(f"Seu saldo é de R${self.__saldo}")
            return self.__saldo