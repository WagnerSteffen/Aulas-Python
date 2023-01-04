contas = []
depositos = []
saldo = 0


def main():
    yn = bool(input("Deseja criar conta ou ver sair? 1 - CC || Enter - sair: "))
    while yn:
        criaConta()
        verSaldo()
        yn = bool(input("Deseja criar conta ou sair? 1- CC || Enter - sair: "))


def criaConta():
    global contas, depositos, saldo
    num_conta = int(input("Digite um número para a conta: "))

    while num_conta in contas:
        print("Número já existente.")
        num_conta = int(input("Digite novamente um número para a conta:"))

    contas.append(num_conta)

    deposito = float(input("Digite o saldo incial da conta: "))
    while deposito <= 0:
        print("Valor de depósito invalido")
        deposito = float(input("Digite o saldo inicial da conta: "))
    depositos.append(deposito)
    saldo += deposito


def verSaldo():
    global saldo
    yn = bool(input("Deseja ver o saldo? 1 - SIM || 0 - NÃO: "))
    if yn:
        print("O saldo do banco é R$%i" % saldo)


main()
