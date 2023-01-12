num = 1000

while num < 10000:
    aux = num

    dois_ult = aux%100

    aux //= 100

    dois_prim = aux%100

    if (dois_ult + dois_prim)**2 == num:
        print(num)

    num += 1
