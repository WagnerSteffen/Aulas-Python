def ConverteHorário(hora):
    return hora - 12

def imprimeHora(hora, minuto):
    if hora <= 12:
        print("%i:%i A.M."%(hora, minuto))
    else:
        hora = ConverteHorário(hora)
        print("%i:%i P.M."%(hora, minuto))

rodando = True
while rodando:
    hora = int(input("Digite a hora: "))
    minuto = int(input("Digite os minutos: "))
    imprimeHora(hora, minuto)
    rodando = bool(int(input("Deseja fazer uma nova conversão(1 - sim/0 - não): ")))
    
