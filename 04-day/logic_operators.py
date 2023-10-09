# Operador "and"
x = int(input("Ingrese un numero: "))
my_bool = 10 < x < 20
print(f"El numero {x} esta entre 10 y 20: {my_bool}")

# Operador "or"
my_bool = x < 10 or x > 20
print(f"El numero {x} es menor que 10 o mayor que 20: {my_bool}")

# Operador "not"
my_bool = not my_bool
print(f"Si negamos el resultado anterior, tenemos: {my_bool}")

# Operador "in" -> funciona con iterables
text = input("Ingrese un texto: ")
word = 'ñero'
word_in_text = word in text
print(f'Esta la palabra "{word}" en el texto ingreasdo: {word_in_text}')
