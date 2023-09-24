"""
FORMATTING
Se refiere a usar valores en un string que originalmente no son de tipo de string. Evitando tener que hacer el casteo
del valor de forma explicita y usando concatenaciones

## Función Format
Permite interporlar los valores que se le pasan en las posiciones donde encuentran el patron "{}".
El reemplazo se hace en orden, es decir, al primer "{}" le corresponde le primer valor pasado a la función, y
asi sucesivamente.
"""
x = 10
y = 5
print("I have two numbers: x = {} and y = {}".format(x, y))

"""
Cadenas Literales
Debido a que la función format resulta poco legible, desde python 3.8, se puede usar la notación f"" para anticipar la
interpolación de variables
"""
me = "Juanes"
language = "Javascript"
print(f"I'm {me} and my main language is {language}")
