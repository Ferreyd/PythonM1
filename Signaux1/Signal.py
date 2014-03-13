__author__ = 'Nicolas'
import math
import matplotlib.pyplot as plt
import numpy as np

class Signal(object):

    """
        On prend les donnees necessaire a la construction de la courbe
    """
    def __init__(self,a,ph,fe,f,nT):
        self.a = a
        self.ph = ph
        self.fe = fe
        self.nT = nT
        self.f = f
        self.T = 1 / self.f
        self.te = 1.0/self.fe
        self.omega = 2*math.pi*self.f
        self.N = int(self.fe/self.f)


    """
        Methode contenant l'algorithme necessaire a la generation de la courbe
    """
    def make(self):

        cos_t = []
        cos_s = []
        for i in range(self.N*self.nT):
            t = self.te*i
            cos_t.append(t)
            cos_s.append(self.fonction(t)) # On prend la fonction de la classe fille
        return cos_t, cos_s


    """
        Affiche la courbe
    """
    def plot(self, inx, iny, title, format='-bo'):
        plt.plot(inx, iny, "-bo", hold=True)
        plt.xlabel('time (s)')
        plt.ylabel('voltage (V)')
        plt.title(title)
        # plt.ylim([-1.2,+1.2])
        plt.grid(True)
        plt.show()



