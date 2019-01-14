#Funcion: Bloque de instruccion que presenta un nombre unico y siempre retorna un valor.

#Declarar funciones
"""
def suma(x,y):
    total = x + y
    return total

print(suma(2,2))


"""
#Parametros default
"""
def login(user="root", password="123"):
    print("User: ", user)
    print("password: ", password)

login()
login("Claudio", 14253)
"""
#Argumentos posicionales (tupla) x nombrados (envio como diccionario)
"""
defs_personales(nombre, appellido,  edad, sexo):
    print("Nombre: {}\nApellido: {}\nEdad: {}\nSexo: {}"
          .format(nombre, appellido, edad, sexo))


datos_personales("Alvaro", "Monserrat", 27, True) #Argumentos posicionales
print("")
datos_personales(edad=25, appellido="Arroyo", sexo=False, nombre="Paula")  #Argumentos nombrados
"""

#Retorno de valores multiples
"""
def func():
    return 20, 10

x, y  = func()

print(x)
print(y)
"""

#Función Variadica: Es toda funcion capaz de recibir catidades variadas de parametros
"""
#argumentos nombrados o posicionales
def lista_de_argumentos(*args):
    print(args)

#argumentos asociativos
def lista_de_argumentos_associativos(**kwargs):
    print(kwargs)

def argumentos(*args, **kwargs):
    print(args)
    print(kwargs)

lista_de_argumentos("hola", "como", "estas")
lista_de_argumentos_associativos(a=1, b =2, c=3, d=4)
lista_de_argumentos_associativos(uno=1, dos =2, tres= 3, cuatro=4)
argumentos(1,2,3,4,5, dia1="lunes", dia2="martes")
"""

#Desempaquetamiento -> lista=[12, 6} - valores empaquetados
"""
lista = [10, 20]

def func(a,b):
    print(a,b)

func(*lista) # el operadaor '*' es de desempaquetamiento
func(lista[0], lista[1])
func(10, 20)
func(a=10, b=20)

"""

#Desempaquetamiento II, funcion zip()
"""
lista = [11, 10 ,12]
tupla = (11, 10 ,12) #La tupla no puede ordenarse

def func(a, b, c):
    print(a)
    print(b)
    print(c)

#lista.sort()
#func(*lista)

#l = [*tupla]
#l.sort()
#func(*l)

z = zip(("a","b","c"),(1,2,3))
print(z)
print(dict(z))

func(**dict(zip(("b","a","c"), tupla)))
"""

#Funciones anidadas
"""
def func():
    print("func")

    def func_interna():
        print("func_interna")

    func_interna()

func()
"""

#Instruccion NONLOCAL: permite acceder a miembros no globales y no locales,
#miembros contenidos en el ambito externo (para funciones anidadas)
"""
a = 4
def func1():
    global a
    a += 2
    b = 2
    print(a)
    def func2():
        nonlocal b
        b += 5
        print(b)
    func2()


func1()
print(a)
"""

#Bloques sin codigos
"""
def function():
    pass

function()
"""
