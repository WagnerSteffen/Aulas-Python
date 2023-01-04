saque = int(input("Digite o valor a ser sacado: "))

cem = saque//100
cinquenta = saque%100//50
dez = saque%50//10
cinco = saque%10//5
um = saque%5//1

if 9 < saque < 601:
    print("Você recebeu",cem,"nota(s) de 100R$")
    if saque % 100 > 0:
            print("Você recebeu",cinquenta,"nota(s) de 50R$")
            if saque % 50 > 0:
                    print("Você recebeu",dez,"nota(s) de 10R$")
                    if saque % 10 > 0:
                            print("Você recebeu",cinco,"nota(s) de 5R$")
                            if saque % 5 > 0:
                                    print("Você recebeu",um,"nota(s) de 1R$")
                                        
                                
                    

else:
    print("O saque deve Conter o valor entre 10 e 600R$")
