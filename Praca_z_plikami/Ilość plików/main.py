#Ilość plików

#Napisz skrypt zliczający ilość plików w katalogu /dev, skorzystaj
# ze standardowej biblioteki - os
import os
# lokalizacja folderu w projekcie

print(os.getcwd())
#FOLDER = "D:\AGH\Programowanie_Python\Praca_z_plikami"
FOLDER=os.getcwd()
totalFiles = 0
totalDir = 0

for base, dirs, files in os.walk(FOLDER):
    for directories in dirs:
         totalDir += 1
    for Files in files:
         totalFiles += 1

print('Ilość plików',totalFiles)
print('Ilość plików + folderów :',(totalDir + totalFiles))
