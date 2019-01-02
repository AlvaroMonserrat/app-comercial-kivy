#Comentario
"""
--------
"""
print("1")

a = int(input("Ingrese un primer numero "))
b = int(input("Ingrese un segundo numero "))

if a > b:
    print("El primer numero %d es mayor que el segundo %d." %(a, b))
elif a < b:
    print("El segundo numero %d es mayor que el primero %d." %(b, a))
else:
    print("Los numeros son iguales a: " + str(a))