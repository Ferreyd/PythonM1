import math
import matplotlib.pyplot as plt
import numpy as np
from Signal import Signal

class SignalTriangle(Signal):

    def __init__(self, a, ph, f, fe, nT):
        self.a = a
        self.ph = ph
        self.fe = fe
        self.nT = nT
        self.f = f
    """
        La fonction d un signal carre
    """
    def fonction(self, t):
        return self.a*(4*(math.fabs(t/self.T-math.floor(t/self.T+0.5)))-1.0)

    """
        Affiche la courbe
    """
    def show(self, titre="Signal Triangle", format='-bo'):
        x,y = self.make()
        self.plot(x,y,titre)




