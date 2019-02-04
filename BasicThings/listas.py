#Extrear elementos de una lista
    #lista[star:stop:step]
"""
lista = "PYTHON"

print(lista[::2]) #imprimir de pasos de a dos
print(lista[2::]) #imptimi desde lista[2] en a delante
print(lista[2::2]) #imptimi desde lista[2] en a delante y en pasos de dos
print(lista[::-1]) #Invertir lista
"""



#Incluir, alterar y extraer
"""

#Incluir
l = ["aaa", "bbb", "ccc"]
l.append("ddd")
print(l)
l.insert(0, "+++")
print(l)
l.insert(1, "---")
print(l)

#Limpiar lista
l.clear()
print(l)

#Remover el ultimo elemento de la lista
l = ["aaa", "bbb", "ccc"]
print(l.pop())
print(l)

#Remover el primer elemento de la lista
print(l.pop(0))
print(l)

#Remover varios elementos
l = ["aaa", "bbb", "ccc", "ddd", "eee"]
del(l[2:4])
print(l)
"""



#Ordenamiento de lista
"""


#Invertir datos de una lista
list_names = ["Paula", "Javiera", "Pedro", "Claudia", "Sofia", "Carlos"]
print(list_names)

list_names.reverse()#Invertir datos de una lista
print(list_names)

list_names.sort()#Ordenar de forma ascendente
print(list_names)

list_names.sort(reverse=True)#Ordenar de forma descendente
print(list_names)
"""


#Lenght, Contar elementos, index
"""
list_nums = [10, 20, 30 ,40 ,50 ,60 ,70 ,60 ,80 ,60]
print(len(list_nums)) #Entrega el numero de elementos de la lista
print(list_nums.count(60)) #Entrega en numero de elementos iguales
print(list_nums.index(30)) #Entrega la posicion del elemento a buscar
"""


#Tuplas ( )

t = tuple("abc")
a = "aaa", 1, True
value = 2
print(t)
print(a)
print(type(a))

x = 10
if x in (1, 5, 10, 20, 30):
    print("El valor esta contenido")
else:

    print("El valor no esta contenido")

