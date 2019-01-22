import BasicThings.modules as mt
#Comentario
"""
--------
"""
print("1")

a = int(input("Ingrese un primer numero "))
b = int(input("Ingrese un segundo numero "))

# Atribucion Multiple

a, b = b, a

x, y, z = 3, 4, 5
x, y, z = x**2, x+y+z, x*y*z

print("x es " + str(x))
print("y es " + str(y))
print("z es " + str(z))
"""
-------------------------------------
"""

if a > b:
    print("El primer numero %d es mayor que el segundo %d." %(a, b))
elif a < b:
    print("El segundo numero %d es mayor que el primero %d." %(b, a))
else:
    print("Los numeros son iguales a: " + str(a))


print(mt.areaCirculo(5))