# Mnożenie macierzy
# Napisz skrypt realizujący mnożenie dwóch macierzy o rozmiarach 8x8
import numpy as np
size = 8
max_number=101
min_number=0
a= np.random.randint(min_number, max_number,(size,size))
#a=np.array([[-1, -2, 3], [0, 2, -1], [-1, 3, 0]])## Sprawdzenie
print("macierz a:")
print(a)
b = np.random.randint(min_number, max_number,(size,size))
#b=np.array([[1, 5, 1], [2, 1, 2], [3, 2, 3]]) ## Sprawdzenie
print("macierz b:")
print(b)
c=np.zeros(shape=(size,size))
for i in range(size):
    for j in range(size):
        for k in range(size):
            c[i][j] = c[i][j] + a[i][k] * b[k][j]
#  prawidlowy wynik c=([[4, -1, 4, [1, 0, 1], [5, -2, 5]]### Sprawdzenie
print("macierz c:")
print(c)