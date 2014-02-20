import math
import matplotlib.pyplot as plt
import numpy as np

def make_carre(a=1.0, ph=0, f=440.0, fe=8000.0, nT=1):
    omega = 2*math.pi*f
    N = int(fe/f)
    te = 1.0/fe
    cos_t = []
    cos_s = []
    for i in range(N*nT):
        t = te*i
        cos_t.append(t)
        cos_s.append(a*signe(math.sin((omega*t)+ph)))
    return cos_t, cos_s


def signe(nb):
    print(nb)
    if(nb > 0):
        return 1
    elif(nb == 0):
        return 0
    elif(nb < 0):
        return -1


def plot(inx, iny, title, format='-bo'):
    plt.plot(inx, iny, "-bo", hold=True)
    plt.xlabel('time (s)')
    plt.ylabel('voltage (V)')
    plt.title(title)
    # plt.ylim([-1.2,+1.2])
    plt.grid(True)

if __name__ == '__main__':

    x,y = make_carre(3,ph=0, f=50.0, fe=1000.0, nT=3)
    plot(x,y,"Un carre ...")
    plt.show()
