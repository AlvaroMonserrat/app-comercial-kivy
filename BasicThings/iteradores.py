"""
---CURSO DE PYTHON--
Capitulo de Iteraciones
"""

# Atribuciones Condicionales (Otra forma de if ():)
"""------------------------------------------------------
value_t = int(input("Ingrese un número mayor que 0: "))
s = "Par" if value_t % 2 == 0 else "Impar"

print("El número ingresado es " + s)
------------------------------------------------------"""

# while
"""------------------------------------------------------
x = 1
while x <= 10:
    print(x)
    x += 1
else:
    print("Fin del Ciclo")
------------------------------------------------------"""

# for var> in <lista> and function -range([start],stop[,step])- -range(stop[)-
"""------------------------------------------------------
for c in range(10, 0, -1):
    if c % 2 == 0:
        continue
    print(c)
    if c == 5:
        break
------------------------------------------------------"""

# Estructura de Datos (7 principales)
# Lista []

lista = ["Hola", 2, 'b', 5, 'c', [0, 1]]
listcharacter = list("Alvaro")

for i in lista:
    print(i)

print("El tercer elemeto de la lista es: "+str(lista[2]))

# Pila
# Array / Matriz / Vector
# Tupla
# Set(Grupo)
# Diccionario
# Arbol
