import math
import matplotlib.pyplot as plt
import numpy as np

class SignalTriangle:

    def __init__(self):
        self = self



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