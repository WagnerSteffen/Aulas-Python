"""
Dizemos que um número natural n é palíndromo (3) se 
    o 1º algarismo de n é igual ao seu último algarismo, 
    o 2º algarismo de n é igual ao penúltimo algarismo, 
    e assim sucessivamente.

Exemplos:
567765 e 32423 são palíndromos.
567675 não é palíndromo.
Dado um número natural   n > 10 , verificar se n é palíndrome.

567765
iguais
567765
"""

#   aux         dig           reverso            n
#   567765       0               0             567765
#----------------------------------------------------
#   567765       5             5
#   56776        6             50 + 6 --> 56
#   5677         7             560 + 7 --> 567
#   567          7             5670 + 7 --> 5677
#   56           6             56770 + 6 --> 56776
#   5            5             567760 + 5 --> 567765
#   0

#  aux//10    aux%10           reverso*10 + dig

n = int(input("Digite um número: "))

aux, reverso = n, 0

while aux != 0:
    reverso = reverso*10 + aux%10  #gerando numero reverso
    aux //= 10 #Diminuindo um digito de aux

if reverso == n:
    print(n, 'é palindromo')
else:
    print(n, 'não é palidromo')
