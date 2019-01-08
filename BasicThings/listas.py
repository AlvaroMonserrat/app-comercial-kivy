#Extrear elementos de una lista
    #lista[star:stop:step]
"""
lista = "PYTHON"

print(lista[::2]) #imprimir de pasos de a dos
print(lista[2::]) #imptimi desde lista[2] en a delante
print(lista[2::2]) #imptimi desde lista[2] en a delante y en pasos de dos
print(lista[::-1]) #Invertir lista
"""

"""
#Incluir, alterar y extraer elementos de una lista
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