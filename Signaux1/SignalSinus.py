import math
import matplotlib.pyplot as plt
import numpy as np
from Signal import Signal

class SignalSinus(Signal):

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
        res = []
        res.append(self.a*math.sin((self.omega*t)+self.ph))
        return res
    """
        Affiche la courbe
    """
    def show(self, titre="Signal Sinus", format='-bo'):
        x,y = self.make()
        self.plot(x,y,titre)