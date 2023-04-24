"""
Tres irmas receberam uma heranca que no total soma 900 reais. Cada uma recebeu
uma quantidade diferente da outra. Se a irma 1 der 1/4 do que recebeu e
a irma 2 der 1/3 do que recebeu para a 3a irma, todas terao o mesmo valor.
Quanto recebeu a irma 1 e a irma 2.
"""


import time

start_time = time.time()

sis1 = list(range(4, 901, 4))
sis2 = list(range(3, 901, 3))

for num1 in sis1:
    num_off1 = num1 - (num1 // 4)
    for num2 in sis2:
        num_off2 = num2 - (num2 // 3)
        sis3 = 900 - (num1 + num2)
        if (
            sis3 > 0
            and num_off1 + num_off2 + (sis3 + (num1 / 4) + (num2 / 3)) == 900
            and sis3 != 0
            and num_off1 == num_off2 == (sis3 + (num1 / 4) + (num2 / 3))
        ):
            print(num1, num2, sis3)


end_time = time.time()
cast_time = end_time - start_time
print(cast_time)
