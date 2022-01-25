# Iloczyn skalarny
# Napisz skrypt obliczający wartość iloczynu dwóch wektorów:
# a = [1, 2, 12, 4], b = [2, 4, 2, 8], tzw. iloczyn skalarny wektorów

a = [1, 2, 12, 4]
b = [2, 4, 2, 8]
tabab = [] * 4
length = len(a)
for i in range(length):
    v = a[i] * b[i]
    tabab.append(v)
print(tabab)