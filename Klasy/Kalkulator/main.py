# Kalkulator
# Wykorzystaj powyzszą klasę do stworzenia prostego kalkulatora, parsującego i wykonującego równanie podane przez
# użytkownika
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

class Calculator():
    def __init__(self):
        self.c1 = Complex()
        self.c2 = Complex()
        self.c3 = Complex()
        print("Wpisz pierwszą liczbę: ")
        self.c1.initComplex()
        print("Wpisz drugą liczbę: ")
        self.c2.initComplex()
        self.action = input("wybierz operację(-, +, *, /): ")

    def actionCalc(self):
        if self.action == '-':
            self.c3.sub(self.c1, self.c2)
            print("wynik: ")
            self.c3.display()
            return self.c3
        elif self.action == '+':
            self.c3.sum(self.c1, self.c2)
            print("wynik: ")
            self.c3.display()
            return self.c3
        elif self.action == '*':
            self.c3.multi(self.c1, self.c2)
            print("wynik: ")
            self.c3.display()
            return self.c3
        elif self.action == '/':
            self.c3.div(self.c1, self.c2)
            print("wynik: ")
            self.c3.display()
while True:
    n1 = Calculator()
    n1.actionCalc()