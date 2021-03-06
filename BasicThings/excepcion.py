"""Excepcion es todo desvio de la regla general"""

"""Tratamiento de Excepcopnes:
es todo codigo que identifica errores e implementa una solucion evitando que la aplicacion
sea finalizada"""

"""Levantamiento de excepciones: 
Es todo codigo que al percibir un problema crea una excepcion avisandole asi al programador"""

"""-------Estructura exception--------
   codigo
except ErrorClass1:
   tratamiento
except ErrorClass2
   tratamiento
------------------------------------"""

"""---------Ejemplo-----------
try:
    a = 10 / 0
    print(a)
except ZeroDivisionError:
    print("Error al dividir por 0")
 ------------------------------"""

"""---------Valores Invalidos-----------

def input_float(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Número inválido.")

def print_zeroError(num1, num2):
    while True:
        try:
            print(num1/num2)
            return
        except ZeroDivisionError:
            print("Error al dividir por cero")
            num2 = input_float("Digite nuevamente el segundo numero: ")



num1 = input_float("Digite el primer numero: ")
num2 = input_float("Digite el segundo numero: ")

print_zeroError(num1, num2)

---------------------------------------------------"""

"""---------Multiples Excepciones-----------"""

def error(x):
    try:
        eval(x)
    except TypeError:
        print("Error: TypeError")
    except NameError as e:
        print("Error: NameError")
        print(type(e))  #Tipo de objeto_
        print(e.args)   #Argumentos del mensaje
        print(e)        #mensaje __str__
    except(ValueError, SyntaxError):
        print("Error: ValueError or SyntaxError")
    else:
        print("No ha ocurrido error")
    finally:
        print("Siempre sera ejecutado")
        print("----------------------")

#TypeError
error("int+int")

#NameError
error("find()")

#ValueError
error("int('a')")

#Value corret
error("print('Python code')")