__author__ = 'Nicolas'
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import tp1_0

def QS(sig_s, vmax, b):
    return sig_s, [0]*len(sig_s)

def plot(inx, iny, title, format='-bo'):
    plt.plot(inx, iny, format)
    plt.xlabel('time (s)')
    plt.ylabel('voltage (V)')
    plt.title(title)
    # plt.ylim([-1.2,+1.2])
    plt.grid(True)


if __name__ == '__main__':
    np.set_printoptions(linewidth=250)
    np.set_printoptions(precision=3, suppress=True)
    a=5.0
    b=3
    step = 2*a/(2**b)

    fe = 2000.0
    f = 50.0
    nT = 2
    x,y = tp1_0.make_sin(a,0,f=f,fe=fe,nT=nT)
    z,err = QS(y,a,b)

    fig = plt.figure(figsize = (12,12))
    ax = fig.add_subplot(1,1,1)
    majorLocator = MultipleLocator(step)
    ax.yaxis.set_major_locator(majorLocator)
    plot(x,y, "", 'bo',l=" Signal ")
    plot(x,z,"",'rs', "Quantized")
    plot(x,err,"",'--x', "Diff")
    plt.title("Sinusoide : Fc=" + str(fe) + ", f=" + str(f) + ", d = " + str(nT))
    plt.legend
    plt.show()


