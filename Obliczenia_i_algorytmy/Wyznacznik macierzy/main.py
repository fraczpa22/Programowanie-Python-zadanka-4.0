# Wyznacznik macierzy
# Napisz skrypt wyliczający wyznacznik macierzy wygenerowanej losowo
import numpy
A = numpy.random.randint(1, 101, (3, 3))
length = len(A)
print(A)
det_A = numpy.linalg.det(A)
print(det_A)