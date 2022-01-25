# XML
# Sparsuj przygotowanego XML (parserem SAX i DOM) i go
# zmodyfikuj np. zmień wartość któregoś tag’a i zapisz do nowego
# pliku
import xml.etree.ElementTree as ET

mytree = ET.parse('1.xml')
myroot = mytree.getroot()
            # print(myroot[0].tag) # 1st child of the root
for x in myroot.iter('genre'):
    a = str(x.text) + 'genre has been added'
    x.text = str(a)
    x.set('updated', 'yes')
mytree.write('new.xml')
