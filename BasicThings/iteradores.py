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

lista = ["Hola", 2, 'b', 5, 'c', ["SI", "NO"]]
listcharacter = list("Alvaro")

for i in lista:
    print(i)

print("El tercer elemeto de la lista es: "+str(lista[2]))
print(lista[5][0])
print(lista[5][1])
print("Numero de elemento de la lista es: " + str(len(lista)))
print("El ultimo elemento de la lista es: " + str(lista[-1]))

"""Añadir un elemento a la lista alfinal"""
lista = lista + [10, 11, 12]
lista = 3*[0] + lista
lista.append(13)

"""Eliminar un elemento de una lista"""
del(lista[3])

lista_num = [100, 200, 300 , 400]
for i in range(len(lista_num)):
    lista_num[i] += 1000

print(lista_num)


for i, item in enumerate(lista_num):
    lista_num[i] += 1000
    print(item)
print(lista_num)

# Pila
# Array / Matriz / Vector
# Tupla
# Set(Grupo)
# Diccionario
# Arbol
