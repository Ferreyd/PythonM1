import math
import matplotlib.pyplot as plt
import numpy as np
from Signal import Signal

class SignalCarre(Signal):

    """
        On prend les donnees necessaire a la construction de la courbe
    """
    def __init__(self, a, ph, f, fe, nT):
        self.a = a
        self.ph = ph
        self.fe = fe
        self.nT = nT
        self.f = f

    """
        Affiche la courbe
    """
    def show(self, titre="Signal Carre", format='-bo'):
        x,y = self.make()
        self.plot(x,y,titre)

    """
        La fonction d un signal carre
    """
    def fonction(self, t):
        res = []
        res.append(self.a*self.signe(math.sin((self.omega*t)+self.ph)))
        return res

    """
        Retourne le signe d'un nombre passe en parametre,
        1 si positif, -1 si negatif, 0 sinon
    """
    def signe(self,nb):
        print(nb)
        if(nb > 0):
            return 1
        elif(nb == 0):
            return 0
        elif(nb < 0):
            return -1


