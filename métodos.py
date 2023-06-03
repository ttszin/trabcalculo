#coding: UTF-8
import math 
from numpy import log as ln




def main(): 
    funcao_bissecao()


def funcao_bissecao():
    k = 1.38e-23                    # Constante de Boltzmann
    q = 1.602e-19                   # Carga elétrica do eletron
    t = 300                         # Temperatura do ambiente em Kelvin
    i2 = 2e-3                       # Corrente de saturação no diodo
    r = 330                         # Resistência no circuito
    v = 6                           # Tensão no circuito


    i = v/r                         
    print(i)

    accuracy = 0.0001

    cal = ln((i/i2)+1) 
    
    vd = (k*t/q)*cal            # t = temperatura do ambiente em kelvin // q = carga elétrica do elétron // i2 = corrente de saturação do diodo // k = 1,38 x 10^-23  
    vr = r*i                               # tensão no resistor = resistencia x tensão
    
    f = vr - vd - v                    # i = corrente no circuito // r = resistência no resistor // k = constante de Boltzmann // 

    return(f)

def bissecao():
    if f(a)*f(b) >= 0:
        print("A função não possui raiz no intervalo fornecido.")
    while(b-a)>=precisao:
        cont = 0
        
        cont+=1        
main()
