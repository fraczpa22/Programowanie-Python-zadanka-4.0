# Równanie kwadratowe
# Napisz skrypt obliczający pierwiastki równania kwadratowego
# w postaci : y = ax2+bx+c. Wejściem skryptu są wartości: a, b, c
import random
import math
#Sprawdzenie
a = 2
b = 7
c = 6
# a = random.randint(1, 11)
# b = random.randint(1, 11)
# c = random.randint(1, 11)


delta = b * b - (4 * a * c)
if delta > 0:
    x1 = (-b - math.sqrt(delta))/ (2 * a)
    x2 = (-b + math.sqrt(delta))/ (2 * a)
    print(f"x1 = {x1} \nx2 = {x2}")
elif delta == 0:
    x3 = (-b) / (2 * a)
    print(x3)
else:
    print("Delta < 0")
