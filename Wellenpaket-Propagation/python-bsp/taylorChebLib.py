
from special_functions import besselj


def taylorCoeff(order, cosFreq):
    if order == 0:
        return 1
    if order % 2 == 1:
        return 0
    
    prefac = cosFreq
    for i in range(1,order):
        prefac*=cosFreq/(i+1)

    return (-1)**(order/2) * prefac

def chebyCoeff(order, freq):
    fac=2
    if order == 0:
        fac = 1
    return fac*(-1j)**(order)*besselj(order, freq)