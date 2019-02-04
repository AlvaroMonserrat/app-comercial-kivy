"""--------------Orientacion a Objetos I-----------------"""

"""---------------Clase-----------------
- Generacion de Multiples Instancias
- Especializacion (herencia/composicion)
- Sobrecarga de Operadores
- Polimorfismo
-----------------------------------------"""

"""Herencia: Reutiliza un codigo a traves de la especializacion de los objetos"""

"""Composicion: Combina expresiones"""

"""Estado: Atributos (varoables) referentes a las clases"""

"""Comportamiento: Funciones que manopulan los estados (variables)"""

"""---------Estructura Jerarquica de Clases------------

BaseException
    SystemExit
    KeyboardInterrupt
    GeneratorExit
    Exception
        AritmeticError
            ZeroDivisionError
        ImportError
        NameError
        ValueError
        
----------------------------------------------------------"""


class Rectang:
    """
    def __init__(self):
        self.width = 0
        self.height = 0
    """
    def __init__(self, x, y):
        self.width = x
        self.height = y

    def area(self):
        return self.width*self.height

    def perimeter(self):
        return self.width*2 + self.height*2


cuad = Rectang(10, 10)
rectangulo = Rectang(20, 5)

cuad.newValue = 6 #Se puede añadir un nuevo miebro al objeto

areaCuad = cuad.area()
periCuad = cuad.perimeter()

areaRect = rectangulo.area()
periRect = rectangulo.perimeter()

print('Cuadrado:')
print(areaCuad)
print(periCuad)


print('')

print('Rectangulo:')
print(areaRect)
print(periRect)