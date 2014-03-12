from Signaux1 import Signal
import math
import matplotlib.pyplot as plt
import numpy as np
__author__ = 'Nicolas'
class SignalCarre(Signal):

    def __init__(self, a, ph, f, fe, nT):
        self.a = a
        self.ph = ph
        self.f = f
        self.fe = fe
        self.nT = nT
        self = self


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


