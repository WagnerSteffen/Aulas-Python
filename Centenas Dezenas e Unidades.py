"""
Faça i, [rpgrama que leia números inteiros menores que 1000 e imprima a
quantidade de centenas, dezenas e unidades do mesmo.
        Observando os termos no plural e a colocação do "e", da vírgula
        entre outros.
"""
# Coisas que preciso definir
# NumeroInput, singular, plural, semantica.

variavel = int(input("Digite um número menor do que 1000: "))

#Definindo centena, dezena e unidade
centena = variavel//100
dezena = variavel%100//10
unidade = variavel%10

#Definindo se singular ou plural

if centena > 1:
    a = str("centenas")
else:
    a = str("centena")
if dezena > 1:
    b = str("dezenas")
else:
    b = str("dezena")
if unidade > 1:
    c = str("unidades")
else:
    c = str("unidade")

#Organizando output
"""resposta = (centena, plural, aditivo, ...)"""
adt = str("e")

if centena == 0:
    if dezena == 0:
        resposta = (unidade, c)
    elif dezena != 0:
        resultado = (dezena, b, unidade, c)
elif dezena != 0:
    if unidade == 0:
        resposta = (centena, a, dezena, b)
    else:
        resposta = (centena, a, dezena, b, unidade, c)
print (resposta)

        
