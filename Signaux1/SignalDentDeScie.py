import math
import matplotlib.pyplot as plt
import numpy as np
from Signal import Signal

class SignalDentDeScie(Signal):

    def __init__(self, a, ph, fe, f, nT):
        self.a = a
        self.ph = ph
        self.fe = fe
        self.nT = nT
        self.f = f
    """
        La fonction d un signal carre
    """
    def fonction(self, t):
        return (2*((t/self.T) - math.floor((t/self.T) - (1/2))))
        """
            Affiche la courbe
        """
    def show(self, titre="Signal Dent de scie", format='-bo'):
        x,y = self.make()
        self.plot(x,y,titre)


