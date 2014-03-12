import SignalCarre

__author__ = 'Nicolas'
import math
import matplotlib.pyplot as plt
import numpy as np

class Signal:
    def __init__(self):
        self = self

    def plot(inx, iny, title, format='-bo'):
        plt.plot(inx, iny, "-bo", hold=True)
        plt.xlabel('time (s)')
        plt.ylabel('voltage (V)')
        plt.title(title)
        # plt.ylim([-1.2,+1.2])
        plt.grid(True)
        x,y = SignalCarre.make_carre(self)