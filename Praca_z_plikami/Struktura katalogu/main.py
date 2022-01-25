#Struktura katalogu
#Napisz rekurencyjne przejście drzewa katalogów i wypisanie
#plików, które znajdują się w eksplorowanej strukturze
#Tree

import os
def find_files( files, dirs=[], extensions=[]):
    new_dirs = []
    for d in dirs:
        try:
            new_dirs += [ os.path.join(d, f) for f in os.listdir(d) ]
        except OSError:
            if os.path.splitext(d)[1] in extensions:
                files.append(d)
        print(d)

    if new_dirs:
        find_files(files, new_dirs, extensions )
    else:
        return

files = []
find_files( files, dirs=["D:\AGH\Programowanie_Python"], extensions=['*.*'] )