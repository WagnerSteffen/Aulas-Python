from collections import deque

lista = [1,2,3,4,5,6]
de = deque(lista)
de.rotate(0)
print(de)
de.rotate(-3)
print(de)
de.rotate(-1)
print(de)