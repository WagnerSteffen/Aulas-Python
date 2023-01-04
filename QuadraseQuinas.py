import random

megasena = list(range(1,61))
megac = quina = quadra = 0

#criando jogo do jogador
confirmacao = True
jogo = []
while confirmacao:
    for i in range(6):
        n = int(input("Digite o número entre 1 e 60 que gostaria de jogar: "))
            
        while n in jogo or 1 < n > 60:
            if 1 < n > 60:
                n = int(input("Digite um número entre 1 e 60: "))
            else:
                n = int(input("Número repetido, por favor digite outro número: "))
        jogo.append(n)
    jogo.sort()
    print("")
    print("O jogo feito foi: ", jogo)
    c = int(input("Confirma o jogo? 1-SIM  0-NÃO: "))
    if c == 1:
        confirmacao = False

#Gerando quantidade de jogos
print("")
testes = int(input("Digite o número de testes que deseja fazer: "))

#Ciclo de reset de jogos e comparações
while testes != 0:
    megab = megasena.copy()
    iguais = 0
#criando o sorteio da mega
    sorteio = []
    for j in range(6):
        num = random.choice(megab)
        sorteio.append(num)
        megab.remove(num)
        sorteio.sort()
#Verificando o tipo de jogo que ganhou
    for k in range(6):
        if jogo[k] == sorteio[k]:
            iguais += 1
    if iguais == 6:
        megac += 1
    elif iguais == 5:
        quina += 1
    elif iguais == 4:
        quadra += 1
    
    testes -= 1

print("")
print("O jogador ganhou %i quadras: "%quadra)
print("O jogador ganhou %i quinas: "%quina)
print("O jogador ganhou %i megas: "%megac)