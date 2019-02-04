"""-----------Encapsulamiento------------
Encapsulamiento: Es el aislamiento de un codigo

Metodo Getters: Siempre retorna valores
Metodo Setters: Siempre reciben valores a traves de parametros

Metodos accesores: Garantizan la integridad de la informacion interna de los objetos

Visibilidad de miembros: Uso de underline "_"
publico = 0
_restricto = 0

Colision de nombres = Para evitar la colision de nombres entre la superclase y la subclase, el
miebro debe estar precedido por dos underlines "__"
__colision = 0

Metodos Magicos: se encuentran precedidos y finalizados por dos underlines (dunders)
y son exclusivos del lenhuaje
__lenguaje__ = " "
"""



class Rectangulo:

    def __init__(self, largo = 1, altura = 1):
        self.set_largo(largo)
        self.set_altura(altura)

    def set_altura(self, num):
        if not((isinstance(num, int) or isinstance(num, float)) and num > 0):
            raise ValueError("Altura es invalida: {}".format(num))
        self._altu = num

    def set_largo(self, num):
        if not ((isinstance(num, int) or isinstance(num, float)) and num > 0):
            raise ValueError("Largo es invalido: {}".format(num))
        self._larg = num

    def get_area(self):
        return self._altu * self._larg

    def get_largo(self):
        return self._larg

    def get_altura(self):
        return self._altu

    def get_rectangulo(self):
        return self._altu, self._larg

    def set_rectangulo(self, largo, altura):
        self.set_largo(largo)
        self.set_altura(altura)

    largo = property(fget=get_largo, fset=set_largo)
    altura = property(fget=get_altura, fset=set_altura)

r = Rectangulo(3, 4)

print("Area: ", r.get_area())
print("Lados:", r.get_rectangulo())

r.set_altura(5)
r.set_largo(6)


print("Area: ", r.get_area())
print("Lados:", r.get_rectangulo())

r.set_rectangulo(10, 10)
print("Area: ", r.get_area())
print("Lados:", r.get_rectangulo())

"""--Propiedades---"""
cuad = Rectangulo()
cuad.altura = 20
cuad.largo = 5

print("Area: ", cuad.get_area())
print("Lados:", cuad.get_rectangulo())
