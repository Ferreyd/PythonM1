import math
import matplotlib.pyplot as plt
import numpy as np

def make_cos(a=1.0, ph=0, f=440.0, fe=8000.0, nT=1):
    omega = 2*math.pi*f
    N = int(fe/f)
    te = 1.0/fe
    cos_t = []
    cos_s = []
    for i in range(N*nT):
        t = te*i
        cos_t.append(t)
        cos_s.append(a*math.cos((omega*t)+ph))

    return cos_t, cos_s

def plot(inx, iny,in2x, in2y,  title, format='-bo'):
    plt.plot(inx, iny, "b.", hold=True)
    plt.plot(in2x, in2y,"r.")
    plt.xlabel('time (s)')
    plt.ylabel('voltage (V)')
    plt.title(title)
    # plt.ylim([-1.2,+1.2])
    plt.grid(True)

if __name__ == '__main__':

    x,y = make_cos(1.5,ph=0, f=50.0, fe=500.0, nT=2)
    x2,y2 = make_cos(0.5,ph =(math.pi), f=50.0, fe=1000.0, nT=2)
    plot(x,y,x2,y2,"deux cosinusoides ...")
    plt.show()
