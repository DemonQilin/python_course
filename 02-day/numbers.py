# Python tiene varios tipos de números, sin embargo, los dos mas comunes son los enteros (int) y flotantes (float).
# La función type sirve para saber el tipo de un valor

# Enteros <int>
# Son numeros que no tienen parte decimal, y sirven para representar contadores. A excepción de la división todas
# las operaciones entre enteros retornan enteros

age = 45
age2 = 26
print("===INTEGERS===")
print(type(age))
print(type(age + age2))
print(type(age - age2))
print(type(age * age2))

# Para obtener un entero en división se debe usar la división entera, mediante el operador "//"
print(type(age / 2))  # división normal retorna float
print(type(age // 2))  # división entera retonar int

# Flotantes <float>
# Numeros que tienen parte fraccionara. Cuando se operan juntos con numeros enteros el resultado sera de tipo <float>
# La división siempre retona numeros de tipo float

temperature = 15.8
samples = 5

print("\n===FLOATS===")
print(type(temperature - 243))
print(type(temperature * samples))
print(type(4 / 5))
