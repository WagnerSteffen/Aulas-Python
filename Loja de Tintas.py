
"""
area ?
tx = 1L/6m
latG = 18 = 80
gal = 4 = 25

comprar apenas latas de 18L?
comprar apenas galoes de 4L?
misturar latas e galoes via preço

10% de folga

"""

print ("Bem vindo")

area = int(input("Digite o tamanho da area a ser pintada: "))

litros = area/6

#se a quantidade de litros for maior que 12
if litros >= 18:
    #Multiplo de 18 +1 gal
    if litros %18 == 0:
        qlat = (litros/18)
        gal = 1
    #Com resto != 0
    if litros %18 != 0:
        qlat = litros//18
        resto = litros %18
        gal = (resto//4)+1
        if gal >= 4:
            gal = 0
            qlat = qlat + 1
#Entre 12 e 18ls
if litros < 18:
    if litros >= 12:
        qlat = 1
        gal = 0
    
#se a quantidade de latas for menor igual a 12
if litros < 12:
    qlat = 0
    gal =(litros//4)+1

#valor final da compra
valor = (qlat*80)+(gal*25)

print ("Voce deverá comprar", int(qlat), "latas de 18L e", int(gal), "galoes de 4L totalizando um total de R$",valor)
