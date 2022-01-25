# Liczby zespolone
# Zdefiniuj klasę reprezentującą liczby zespolone
# (wraz z funkcjami na nich działającymi np. dodawanie, odejmowanie itd.)

class Complex ():
    def initComplex(self):
        self.realPart = int(input("Wpisz część rzeczywistą: "))
        self.imgPart = int(input("Wpisz część urojoną: "))
    def display(self):
        if self.imgPart<0  :
            print(self.realPart,self.imgPart,"i", sep="")
        else:
            print(self.realPart, "+", self.imgPart, "i", sep="")
    def sum(self, c1, c2):
        self.realPart = c1.realPart + c2.realPart
        self.imgPart = c1.imgPart + c2.imgPart
    def sub(self, c1, c2):
        self.realPart = c1.realPart - c2.realPart
        self.imgPart = c1.imgPart - c2.imgPart
    def multi(self, c1, c2):
        self.realPart = (c1.realPart * c2.realPart )+(c1.imgPart * c2.imgPart*-1)
        self.imgPart = (c1.realPart * c2.imgPart)+(c1.imgPart * c2.realPart)
    def div(self, c1, c2):
        self.realPart = ((c1.realPart * c2.realPart) + (c1.imgPart * c2.imgPart ))/((c2.realPart * c2.realPart) + (c2.imgPart * c2.imgPart ))
        self.imgPart = ((c1.imgPart * c2.realPart) - (c1.realPart * c2.imgPart ))/((c2.realPart * c2.realPart) + (c2.imgPart * c2.imgPart ))


c1 = Complex()
c2 = Complex()
c3 = Complex()
print("Wpisz pierwszą liczbę")
c1.initComplex()
print("Pierwsza liczba: ", end="")
c1.display()
print("Wpisz drugą liczbę")
c2.initComplex()
print("Druga liczba: ", end="")
c2.display()
print("Suma dwóch liczb: ", end="")
c3.sum(c1,c2)
c3.display()
print("Różnica dwóch liczb:  ", end="")
c3.sub(c1,c2)
c3.display()
print("Mnożenie dwóch liczb: ", end="")
c3.multi(c1,c2)
c3.display()
