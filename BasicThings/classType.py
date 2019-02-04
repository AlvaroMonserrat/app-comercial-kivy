"""-------------------Objeto Clase-------------------
-Class
    - NameClass
        - ObjectClass
"""
"""
class MiClase:
    pass

obj = MiClase()

print(type(obj)) #Instancia de Clase
print(type(MiClase)) #Objeto Clase

from pprint import  pprint

pprint(MiClase.__dict__)
"""

class MiClase:
    miembro_cls = 50

    def __init__(self):
        self.miembro_inst = -10

    def func(self):
        print(self.miembro_inst)   #Miembro de instancia
        print(self.miembro_cls)    #Instancia self
        print(MiClase.miembro_cls) #Objeto Clase

"""
i1 = MiClase()
i1.func()
#print(i1.miembro_inst)
#print(i1.miembro_cls)
#print(MiClase.miembro_cls)
"""

i1 = MiClase()
i2 = MiClase()
i1.miembro_cls = 10
print("i1: "+str(i1.miembro_cls))
print("i2: "+str(i2.miembro_cls))

MiClase.miembro_cls = 9
del(i1.miembro_cls)

print("-------")
print("i1: "+str(i1.miembro_cls))
print("i2: "+str(i2.miembro_cls))