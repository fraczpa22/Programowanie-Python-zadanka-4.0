import matplotlib.pyplot as plt
import numpy as np
import threading

class AXS1(threading.Thread):
    def run(self):
        while True:
            global h1
            h1 = np.random.normal(170, 10, 250)

class AXS2(threading.Thread):
    def run(self):
        while True:
            global h2
            h2 = np.random.normal(170, 10, 250)
class AXS3(threading.Thread):
    def run(self):
        while True:
            global h3
            h3 = np.random.normal(170, 10, 250)

class AXS4(threading.Thread):
    def run(self):
        while True:
            global h4
            h4 = np.random.normal(170, 10, 250)
class PLOTING(threading.Thread):
    def run(self):

        while True:
            plt.subplot(2, 2, 1)
            plt.hist(h1, color="k")
            plt.subplot(2, 2, 2)
            plt.hist(h2, color="r")
            plt.subplot(2, 2, 3)
            plt.hist(h3, color="g")
            plt.subplot(2, 2, 4)
            plt.hist(h4, color="y")

            plt.draw()
            plt.pause(0.1)
            plt.clf()
plt.ion()
def main():

    hist1 = AXS1()
    hist1.start()
    hist2 = AXS2()
    hist2.start()
    hist3 = AXS3()
    hist3.start()
    hist4 = AXS4()
    hist4.start()
    ploter = PLOTING()
    ploter.start()

main()
