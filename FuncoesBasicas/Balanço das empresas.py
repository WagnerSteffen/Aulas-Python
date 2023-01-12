
n = int(input("Digite o numero de empresas: "))
m = int(input("Digite o numero de meses: "))

empresa = 1

while empresa <= n:
    mes = 1
    print ("Empresa", empresa, ":")
    balança = 0
    while mes <= m:
        print("Mês", mes, ":")
        ganho = int(input("Digite os ganhos da empresa: "))
        gasto = int(input("Digite os gastos da empresa: "))
        balança = balança + (ganho - gasto)
        print ("")
        mes = mes+1
    if balança == 0:
        print("A empresa", empresa, "fechou com um balanço de R$ 0")
    elif balança > 0:
        print("A empresa", empresa, "fechou com um balanço de R$", balança)
    else:
        print("A empresa", empresa, "fechou com um déficete de R$", balança)

    empresa = empresa+1
    print("")
