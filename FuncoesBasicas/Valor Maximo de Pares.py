
m = int(input('M: '))
n = int(input('N: '))
fant,xx, yy = ( 0, 0, 0)
for x in range(m):
    for y in range(n):
        if (x*y) - (x**y) + y > fant:
            fant = (x*y) - (x**y) + y
            xx = x
            yy = y
print(fant)
