import Signaux1
from Signaux1.SignalCarre import SignalCarre

if __name__ == '__main__':

    SignalCarre(3,0,50.0,1000.0,3).


    x,y = make_carre(3,ph=0, f=50.0, fe=1000.0, nT=3)
    plot(x,y,"Un carre ...")
    plt.show()