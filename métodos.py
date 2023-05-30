#coding: UTF-8
import math 

def main():
    funcao()


def funcao():
    k = 1.38*10**-23
    q = 1.602*10**-19
    t = 300
    i2 = 2
    r = 330
    v = 6
    
    vd = k*t/q.log((i/i2)+1)             # t = temperatura do ambiente em kelvin // q = carga elétrica do elétron // i2 = corrente de saturação do diodo // k = 1,38 x 10^-23  
    vr = r*i
    f = vr - vd - i*r                    # i = corrente no circuito // r = resistência no resistor // k = constante de Boltzmann // 






main()