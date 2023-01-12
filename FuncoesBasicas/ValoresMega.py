import random

megasena = list(range(1,61))
cont = megac = quina = quadra = 0
premioquadra = premioquina = premiomega = 0
confirmacao = True
jogo = []
keep = True
sorteio = []
somaquadra = somaquina = somamega = 0

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

while sorteio != jogo:
    sorteio = []
    premio = random.uniform((1.5*(10**6)),(70*(10**6)))
    megab = megasena.copy()
    for i in range(6):
        num = random.choice(megab)
        sorteio.append(num)
        megab.remove(num)
    sorteio.sort()

    iguais = 0
    for j in range(6):
        if jogo[j] == sorteio[j]:
            iguais += 1
    if iguais == 6:
        megac += 1
        premiomega = premio*0.94
        somamega += premiomega
    elif iguais == 5:
        quina += 1
        premioquina = premio*(random.uniform(0.1, 0.4))
        somaquina += premioquina
    elif iguais == 4:
        quadra += 1
        premioquadra = premio*(random.uniform(1/30000, 1/5000))
        somaquadra += premioquadra
    cont += 1

valorinv = cont*4.5

print("")
print("O valor investido foi de %i: "%valorinv)
print("Você receberia as seguintes premiações")
print("Na Quadra: R$%.2f"%somaquadra)
print("Na Quina: R$%.2f"%somaquina)
print("Na Mega: R$%.2f"%somamega)
print("")
print("Número de jogos: %i"%cont)