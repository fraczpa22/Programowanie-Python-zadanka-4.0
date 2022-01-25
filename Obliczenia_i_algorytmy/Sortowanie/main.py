# Sortowanie
# Napisz skrypt sortujący liczby malejąco. Wygeneruj losowo 50
# liczb - wykorzystąj standardową funkcje do losowania.
# Z wbudowanej funkcji sortującej korzystaj tylko w celu weryfikacji
# wyników

import random

alist = []
for i in range(50):
    #losowanie bez powtorzeń
    los = random.randint(1, 1000)
    while los in alist:
        los = random.randint(1, 1000)
    alist.append(los)

print(alist)

for i in range(len(alist)-1):
    for j in range(len(alist)-1-i):
        if alist[j] > alist[j+1]:
            alist[j], alist[j+1] = alist[j+1], alist[j]

print(alist)