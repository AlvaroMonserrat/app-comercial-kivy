#import numpy as np

#f(x) = 1 -> si w*x - u > 0
#f(x) = 0 -> Otro caso

""" Entradas y salidas esperadas:

        a & b & c  =  z
        1   0   0  =  0
        1   0   1  =  0
        1   1   0  =  0
        1   1   1  =  1

"""

tasa_aprend = 0.1
umbral = 0.5
entradas = [[1.0, 0.0, 0.0], [1.0, 0.0, 1.0], [1.0, 1.0, 0.0], [1.0, 1.0, 1.0]]
pesos = [-0.9, 1.0, 0.5]

salidaEsperada = [1.0, 1.0, 1.0, 0.0]

def productoPunto(listaA, listaB):
    resultado = 0
    i = 0
    for a in listaA:
        resultado = resultado + listaA[i]*listaB[i]
        i = i + 1
    return resultado


def sumaListas(a, b):
    s = []
    for i in range(len(a)):
        s.append(a[i] + b[i])
    return s


def multplicarConst(listaA, const):
    t = []
    for i in range(len(listaA)):
        t.append(listaA[i]*const)
    return t

#Aprendizaje

k = 0
y = 0
while y < len(salidaEsperada)+1:

    if(productoPunto(pesos, entradas[k]) > umbral):
        salida = 1
    else:
        salida = 0

    error = salidaEsperada[k] - salida
    z = multplicarConst(entradas[k], error*tasa_aprend)
    print(salida)
    pesos = sumaListas(pesos, z)
    k += 1
    y += 1

    if k == 4:
        k = 0

    if y == len(salidaEsperada):
        print(error)
        if error != 0:
            y = 0
            k = 0


print(pesos)

"""
#Test
k = 0
pesos = [1.5, -0.8, -0.39999999999999997]
for k in range(len(entradas)):
    if productoPunto(pesos, entradas[k]) >  umbral:
        salida = 1
    else:
        salida = 0
    
    print(salida)

"""