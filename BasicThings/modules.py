from math import pi


def areaCirculo(radio):
    print("El area del circulo de radio", radio, "es igual a:")
    result = pow(radio, 2) * pi
    return result

def areaRectangulo(x,y):
    print("El area del rectagulo de lados", x, "y", y, "es igual a:")
    result = x * y
    return result

print(areaRectangulo(2,3))