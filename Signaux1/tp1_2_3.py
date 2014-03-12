__author__ = 'Nicolas'

import math
import matplotlib.pyplot as plt
import numpy as np

def make_triangle(a=1.0, ph=0, f=440.0, fe=8000.0, nT=1):
    omega = 2*math.pi*f
    N = int(fe/f)
    te = 1.0/fe
    T = 1/f
    cos_t = []
    cos_s = []
    for i in range(N*nT):
        t = te*i
        cos_t.append(t)
        cos_s.append(a*(4*(math.fabs(t/T-math.floor(t/T+0.5)))-1.0))
    return cos_t, cos_s

def plot(inx, iny, title, format='-bo'):
    plt.plot(inx, iny, "-bo", hold=True)
    plt.xlabel('time (s)')
    plt.ylabel('voltage (V)')
    plt.title(title)
    # plt.ylim([-1.2,+1.2])
    plt.grid(True)

if __name__ == '__main__':

    x,y = make_triangle(3.0,ph=0, f=50.0, fe=1000.0, nT=2)
    plot(x,y,"Un Triangle ...")
    plt.show()
