# Suma macierzy
# Napisz skrypt sumujący dwie macierze o rozmiarach 128x128.
# Wykorzystaj generator liczb losowych do wygenerowania
# macierzy.
import numpy as np
size = 128
max_number=101
min_number=0
a = np.random.randint(min_number, max_number,(size,size))
print("macierz a:")
print(a)

b = np.random.randint(min_number, max_number,(size,size))
print("macierz b:")
print(b)

c = np.zeros(shape=(size,size))
for i in np.arange(size):
    for j in np.arange(size):
        c[i][j] = a[i][j] + b[i][j]
print("macierz c:")
print(c)
