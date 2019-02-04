"""--------------------------Propiedades-----------------------------

Es un recurso utilizado en la declaracion de miembros publicos que
permite invocar metodos para la lectura y escritura de valores

#Escritura
Instancia.attr = 0

#Lectura
x = instancia.atrr

Funcion property()
property(fget, fset, fdel, doc)

-------------------------------------------------------------------"""
"""--------------Decorators----------------
El Decorador de metodos adiciona funcionalidades a los metodos sin 
alterar su implementacion
@property -> Getter
@variable.setter -> Setter
-----------------------------------------"""


# --------------Property--------------
class A:
    def __init__(self):
        self._var = 0

    def _get_var(self):
        return self._var

    def _set_var(self, x):
        self._var = x

    var = property(fget=_get_var, fset=_set_var)


# --------------Decorators--------------
class B:
    def __init__(self):
        self._var = 0

    @property
    def var(self):
        return self._var

    @var.setter
    def var(self, val):
        self._var = val

# -Property-
a = A()
a.var = 105
print(a.var)

# -Decorators-
b = B()
b.x = 200
print(b.x)
