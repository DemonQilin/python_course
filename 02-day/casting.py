# En Python existen dos tipos de conversiones: las implicitas y las explicitas

"""
IMPLICITAS
Las conversiones implicitas se refiere a las que hace el lenguaje automaticamente cuando se encuentran con operaciones
que involucran valores de distintos tipos.

Un ejemplo tipico es al operar con numberos de tipo <int> y <float>, python internamente convierte los int en floats.
"""

weight = 45.8
print(weight * 3)
print(type(weight * 3))

"""
EXPLICITAS
Las conversiones explicitas se refieren a los cambios de tipo que se le pide a Python que haga desde el codigo.
"""

# Convertir <float> en <int>, en este caso es importante notar que que la conversión no redondea
num1 = 13.6
print(num1)
print(type(num1))

num1 = int(num1)
print(num1)
print(type(num1))

# Convertir un numero ingresado por el usuario, con input, en un valor numerico con el que se pueda operar
age = input("Type your age: ")
print(type(age))

age = int(age)
print(type(age))

nextAge = age + 1
print(nextAge)