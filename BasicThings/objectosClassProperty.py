"""--------------------------Propiedades-----------------------------

--------------------------------------------------------------------"""


class Rectangulo:

    def __init__(self, largo=1, altura=1):
        self._set_largo(largo)
        self._set_altura(altura)

    def _set_altura(self, num):
        if not ((isinstance(num, int) or isinstance(num, float)) and num > 0):
            raise ValueError("Altura es invalida: {}".format(num))
        self._altu = num

    def _set_largo(self, num):
        if not ((isinstance(num, int) or isinstance(num, float)) and num > 0):
            raise ValueError("Largo es invalido: {}".format(num))
        self._larg = num

    def set_rectangulo(self, largo, altura):
        self._set_largo(largo)
        self._set_altura(altura)

    def _get_area(self):
        return self._altu * self._larg

    def _get_largo(self):
        return self._larg

    def _get_altura(self):
        return self._altu

    def _get_rectangulo(self):
        return self._altu, self._larg

    largo = property(fget=_get_largo, fset=_set_largo)
    altura = property(fget=_get_altura, fset=_set_altura)
    area = property(fget=_get_area)
    rectangulo = property(fget=_get_rectangulo)


class Triangulo:

    def __init__(self, base=1, altura=1):
        self._base = base
        self._altura = altura

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, value):
        if not((isinstance(value, int) or isinstance(value, float)) and value > 0):
            raise ValueError("Base no valida: {}".format(value))
        self._base = value

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, value):
        if not((isinstance(value, int) or isinstance(value, float)) and value > 0):
            raise ValueError("Altura no valida: {}".format(value))
        self._altura = value

    @property
    def area(self):
        return (self._base * self._altura)/2

"""-----------------CODE------------------"""
# Crear instancia
rect = Rectangulo(5, 20)
# Set largo
rect.largo = 10
# Print largo y alto
print(rect.rectangulo)
# Print Area
print(rect.area)

# Crear instancia
triang = Triangulo(5, 3)
# Set largo
triang.base = 10
triang.altura = 5
# Print base y altura
print(triang.base)
print(triang.altura)
# Print Area
print(triang.area)