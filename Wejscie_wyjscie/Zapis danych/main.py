# Zapis danych
# Napisz skrypt realizujący funkcję zamka szyfrowego. Prosi
# o podanie kodu i następnie sprawdza czy jest on zgodny z
# wcześniej wprowadzonym kodem
import hashlib

try:
       plik = open("kod.txt")
       kod = plik.read()
       plik.close()
       jest = True
except:
       jest = False

if jest:
       kod2 = "ala"
       result2 = hashlib.md5(kod2.encode())
       result2 = result2.hexdigest()
       while kod != result2:
           print("zły kod !!!")
           kod2 = input("Podaj kod zamka, (4 cyfry np. 1111):")
           result2 = hashlib.md5(kod2.encode())
           result2 = result2.hexdigest()
           print(kod)
           print(result2)
       print("OK")
else:
       kod2 = input("Ustaw kod zamka, (4 cyfry np. 1111):")
       result2 = hashlib.md5(kod2.encode())
       result2 = result2.hexdigest()

plik = open("kod.txt", "w") # zapisany kod - aby ustawić kod trzeba usunąć plik txt z zapisanym kodem
plik.write(str(result2))
plik.close()

