# Podmienianie słów
# Napisz skrypt zmieniający w podanym ciągu wejściowym
# (wybierz kilka plików z repozytorium: Tekstowego) następujące
# słowa : i, oraz, nigdy, dlaczego na następujący zestaw słów : oraz,
# i, prawie nigdy, czemu. Zalecaną strukturą jest słownik.

# tablica indeksów słów zmienianych
#
# 1. szukamy slowa
# 2. jesli znalezione - pozycja znaku
#     jeśli było zmieniane to opuszczamy
#     w przeciwnym razie zmieniamy i dodajemy znacznik pozycji słowa
import re

keys = { "oraz": "i", "i": "oraz", "nigdy": "prawie nigdy", "dlaczego": "czemu"}
plik = open("tekst.txt", 'r', encoding="utf8")
content = plik.read().splitlines()
plik.close()

marks = []  #tablica indeksów zmienianych wyrazów
for i in range(len(content)):
    marks.append([i])

for key in keys.keys():
    s = len(key.split())
    for i in range(len(content)):
        row = re.findall(r"[\w']+", content[i])  #splitowanie bez przecinków i kropek
        tab = []
        #wyszukanie pozycji wszystkich wyrazów - kluczy w wierszu
        get_indexes = lambda row, xs: [i for (y, i) in zip(xs, range(len(xs))) if row == y]
        indexes = get_indexes(key, row)
        # print(key, get_indexes(key, row))
        # sprawdzenie, czy słowo było zmieniane
        for x in indexes:
            if x not in marks[i][1:]: #wyszukanie oprócz pierwszego elementu, który jest numerem wiersza
                tab.append(x)
                row[x] = keys[key]
        marks[i] = marks[i] + tab
        row = ' '.join(row)
        content[i] = row


plik = open("output.txt", 'w', encoding="utf8")
for row in content:
    plik.write(row+"\n")
plik.close()