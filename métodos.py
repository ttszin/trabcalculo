#coding: UTF-8
import math 
from numpy import log as ln

def main():
    funcao()


def funcao():
    k = 1.38*10**-23
    q = 1.602*10**-19
    t = 300
    i2 = 2
    r = 330
    v = 6


    i = v/r
    print(i)

    accuracy = 0.0001

    cal = ln((i/i2)+1) 
    
    vd = (k*t/q)*cal            # t = temperatura do ambiente em kelvin // q = carga elétrica do elétron // i2 = corrente de saturação do diodo // k = 1,38 x 10^-23  
    vr = r*i                               # tensão no resistor = resistencia x tensão
    
    f = vr - vd - i*r                    # i = corrente no circuito // r = resistência no resistor // k = constante de Boltzmann // 

    print(vd)
    print(vr)
    print(f)






main()