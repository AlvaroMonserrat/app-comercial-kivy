"""Etapas de importacion de modulos"""
#Localizacion
#Compilacion
#Ejecucion

import dis
from math import pi

print(__name__)

def areaCirculo(radio):
    print("El area del circulo de radio", radio, "es igual a:")
    result = pow(radio, 2) * pi
    return result

def areaRectangulo(x,y):
    print("El area del rectagulo de lados", x, "y", y, "es igual a:")
    result = x * y
    return result

#byte code de la funcion areaCirculo
dis.dis(areaCirculo)

