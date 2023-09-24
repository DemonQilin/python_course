# Una variable es un espacio en memoria que se reserva para que el programa pueda almacenar un valor que puede cambiar
# Lo interesante de las variables es que pueden cambiar su valor dinamicamente

# REGLAS NOMBRES
# 1 - Debe ser legible
# 2 - Debe ser una unica unidad de texto: nombre de mi variables => nombre_de_mi_variable
# 3 - Evitar acentos y la ñ
# 4 - El nombre de la variable puede tener números pero no al inicio
# 5 - Casi ningun simbolo, aparte del guin bajo, puede estar
# 6 - No deben ser palabras reservadas como: input, print, int, float

# Cambiando valor
customer = "Cris Oriana"
print("Customer is " + customer)

customer = "Sharith"
print("Customer is " + customer)

# Almacenando string
my_name = "Juanes"
relation = input("Who is Juanes for you?: ")
print(my_name + " is a " + relation + " for you")

# Almacenando numeros
age = 22
print(age)

# Variables calculadas a partir de otras
price = 40.5
iva = 2.2
total = price + iva
print(total)
