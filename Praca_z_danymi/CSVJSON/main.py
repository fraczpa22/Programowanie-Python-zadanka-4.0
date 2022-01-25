# CSV/JSON
# Napisz program proszący użytkownika o dane zawierające kilka
# pól (może to być np. lista zadań z opisem i terminami wykonania czy
# baza recenzji filmów) i zapisujący podane dane do pliku
# w wybranym formacie (CSV/JSON). Przy każdym uruchomieniu program
# powinien odczytywać i wyświetlać wprowadzone
# wcześniej dane, umożliwiać ich usunięcie (po jednym wpisie)
# oraz dodanie nowych rekordów
import csv

lines = list()
with open('3.csv', 'r', encoding="utf-8", newline='' ) as readFile:
    reader = csv.reader(readFile)
    for row in reader:
        lines.append(row)
        print(row)
        try:
            id = int(row[0]) + 1
        except:
            pass
readFile.close()
odp = input("czy usunac wpis?(y/n):")
if odp == "y":
    numer = input("Podaj numer id:")
    for row in lines:
        if row[0] == numer:
            lines.remove(row)
            break
odp = input("czy dodać dane ?(y/n):")
if odp == "y":
        tyt = input("Podaj tytuł:")
        oc = input("Podaj ocenę:")
        lines.append([id, tyt, oc])

with open('3.csv', 'w', encoding="utf-8", newline='') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(lines)
writeFile.close()