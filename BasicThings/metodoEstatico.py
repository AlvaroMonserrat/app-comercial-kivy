"""Metodos estaticos
Es cualquier metodo declarado en la clase conteniendo a cualquier parametro

Funcion staticmethod()

Clase A:
    def func():
        pass
    func = staticmethod(func)

-----------------------------------

Clase A:
    @staticmethod
    def func(arg1, arg2, ...):
        pass

"""

class MEstatico:
    @staticmethod
    def func1():
        print("func1()")

    @staticmethod
    def func2(x, y):
        print("Funcion '{}' invocada. \nParams = ({}, {})".format("func2",x ,y))

    @staticmethod
    def func3(a, b, c):
        info = """
        Nombre de la funcion: {nombre}
        Cuantidad de argumentos: {cantidad}
        Args: {args}
        """
        info = info.format(
            nombre=MEstatico.func3.__name__,
            cantidad=MEstatico.func3.__code__.co_argcount,
            args=MEstatico.func3.__code__.co_varnames
        )
        print(info)

    #func1 = staticmethod(func1)
    #func2 = staticmethod(func2)
    #func3 = staticmethod(func3)

me = MEstatico()
me.func1()
me.func2(2, 3)
me.func3(5, 5, 10)