"""Metodo de clase
Son recursos que se pueden obtener en toda las instancias

Funcion classmethod()

--------------------------------
class A:
    def func(cls, arg1, arg2):
        pass
    func = classmethod(func)
--------------------------------

--------------------------------
class A:
    @classmethod
    def func(cls, arg1, arg2):
        pass
--------------------------------

"""

class Bichos:
    qt_bichos = 0
    def __init__(self):
        self.add_bichos()

    def __del__(self):
        self.del_bichos()
        if(self.qt_bichos == 0):
            print("Todos los bichos estan muertos!")

    @classmethod
    def add_bichos(cls):
        cls.qt_bichos += 1

    @classmethod
    def del_bichos(cls):
        cls.qt_bichos -= 1

    #add_bichos = classmethod(add_bichos)
    #del_bichos =classmethod(del_bichos)


b1 = Bichos()
print(Bichos.qt_bichos)
b2 = Bichos()
print(Bichos.qt_bichos)
b3 = Bichos()
print(Bichos.qt_bichos)

del(b1)
print(Bichos.qt_bichos)
del(b2)
print(Bichos.qt_bichos)
del(b3)
print(Bichos.qt_bichos)