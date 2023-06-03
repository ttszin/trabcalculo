#coding: UTF-8
import math 
from numpy import log as ln




def main(): 
    global accuracy
    global a
    global b

    accuracy = 0.0001
    a = 0.0
    b = 0.05
    corrente_bissecao = bissecao(a,b,funcao_bissecao,accuracy)

    print(f"O valor da corrente elétrica no circuito pelo método da bisseção é : {c} com o total de {cont} iterações")


def funcao_bissecao(i):
    k = 1.38e-23                    # Constante de Boltzmann
    q = 1.602e-19                   # Carga elétrica do eletron
    t = 300                         # Temperatura do ambiente em Kelvin
    i2 = 2e-3                       # Corrente de saturação no diodo
    r = 330                         # Resistência no circuito
    v = 6                           # Tensão no circuito                    

 
    
    vd = math.exp((q*i)/(k*t)) - 1           # t = temperatura do ambiente em kelvin // q = carga elétrica do elétron // i2 = corrente de saturação do diodo // k = 1,38 x 10^-23  
    vr = r*i                               # tensão no resistor = resistencia x tensão
    
    f = vr - vd - v                    # i = corrente no circuito // r = resistência no resistor // k = constante de Boltzmann // 

    return(f)

def bissecao(a,b,f,accuracy):
    global c 
    global cont
    cont = 1    
    if f(a)*f(b) >= 0:
        print("A função não possui raiz no intervalo fornecido.")
    while(b-a)>=accuracy:
        
        c = (b+a)/2

        if f(c) == 0 :
            break 
        elif(f(a)+f(b) < 0):
            b = c
        else:
            a = c

        cont+=1
    return c,cont    
    
main()
