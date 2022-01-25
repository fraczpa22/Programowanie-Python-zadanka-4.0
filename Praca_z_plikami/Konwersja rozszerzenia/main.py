#Konwersja rozszerzenia
#Napisz skrypt konwersji rozszerzeń plików *.jpg na *.png
# (uprzednio stwórz zestaw 4 plików z rozszerzeniem *.jpg)

from PIL import Image

for i in  ["1", "2", "3", "4"]:
    image = Image.open(i+".jpg")
    image.save("zdjecie"+ i+".png")