#diccionarios: Tipo de lista no ordenada en la cual cada elemento está asociado a una llave

"""
    LLave |    Valor
    "a"   |   "Primero"
    "33"  |   "Segundo"
     5    |   "Tercero"
   (10,20)|   "Cuarto"
"""

#Declarar diccionario
"""
dic1 = {}
dic2 = dict()

dic1["aaa"] = 1000
dic1["bbb"] = 2000
dic1["ccc"] = 3000
dic1["ddd"] = 4000

print(dic1)
print(dic1["ccc"])

dic2 = {1.1: "Test1", 2.2: "Test2", 3.3: "Test3"}
print(dic2)
"""


tel = {30301122: "Paula", 33547877: "Claudia", 33381245: "Barbara", 36458899: "Javier"}
print(len(tel))
print(tel)

print(tel.get(36458899)) #Retorna un valor del diccionario

del(tel[36458899]) #Elimina un valor

print(tel)
print(len(tel))
print(tel.keys()) #Retorna la lista de llaves
print(tel.values()) #Retorna los valores

print(tel.popitem()) #Remueve un elemento del diccionario
print(tel)

print(30301122 in tel) #Verificar si se encuentra un valor dentro de un diccionario

tel2 = {999999: "Teste1", 5111551: "Teste2"}

tel.update(tel2) #Añadir elementos a un dicionario
print(tel)

t = (10, 10, 10)
tel[t] = "Hola"  #Añadir una tupla y un elemento al diccionario
print(tel)