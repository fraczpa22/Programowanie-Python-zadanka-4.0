# #Usuwanie słów # link nie działa do repozytorium tesktowego
# Napisz skrypt usuwający z wejściowego ciągu tekstowego
# (wybierz kilka plików z repozytorium: Tekstowego) następujące
# słowa : się, i, oraz, nigdy, dlaczego

words = ["się", "i", "oraz", "nigdy", "dlaczego"]

plik = open("tekst.txt", 'r', encoding="utf8")
content = plik.read()
plik.close()

for word in words:
    word = " "+word+" "
    content = content.replace(word, " ")

plik = open("output.txt", 'w', encoding="utf8")
plik.write(content)
plik.close()