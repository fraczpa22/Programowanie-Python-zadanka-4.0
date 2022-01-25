import threading
import time

class Filozof(threading.Thread):
    kontynuacja = True
    def __init__(self, id, widelec1, widelec2):
        threading.Thread.__init__(self)
        self.id = id
        self.widelecLewy = widelec1
        self.widelecPrawy = widelec2

    def run(self):
        while self.kontynuacja:
            print('Osoba', self.id, 'myśli')
            time.sleep(1)
            w1 = self.widelecLewy
            w2 =self.widelecPrawy
            while self.kontynuacja:
                w1.acquire()
                if w2.acquire(False): break
                w1.release()
                w1, w2 = w2, w1
                time.sleep(0.5)
            else:
                return
            print(' Osoba', self.id, 'je')
            time.sleep(1)
            w2.release()
            w1.release()

def main():
    widelec = [threading.Semaphore() for n in range(5)]
    osoby=[Filozof(1,widelec[0],widelec[1]),
                Filozof(2,widelec[1],widelec[2]),
                Filozof(3,widelec[2],widelec[3]),
                Filozof(4,widelec[3],widelec[4]),
                Filozof(5,widelec[4],widelec[0])]
    for id in osoby: id.start()
    time.sleep(10)
    Filozof.kontynuacja = False
main()