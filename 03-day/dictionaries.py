# Creación
my_dictionary = {'gonorrea': 'Algo muy malo', 'chimba': 'Algo muy bueno'}
print(f"Tipo de un diccionario: {type(my_dictionary)}")
print(my_dictionary)

# Lectura
gonorrea = my_dictionary['gonorrea']
print(f"my_dictionay[\"gonorrea\"] is: {gonorrea}")

"""
El ejemplo de cliente nos permite ver que un diccionario puede almacenar cualquier tipo de dato como valor.
"""
client = {'nombre': 'Juanes', 'apellido': 'Velez', 'edad': 28, 'estatura': 1.63}
print(f"\nEl cliente es:\n{client}")

target_field = input("Which field you want to know it?\n> ")
print(client[target_field])

# Ejemplo con estructuras compuestas como valores
dic = {'list': [1, 2, 3, 4], 'dict': {'a': 1, 'b': 2, 'c': 3}}
print(f"\nDictionary with complex data:\n{dic}")
print(f"El valor de dic['list'][2] es: {dic['list'][2]}")

# Ejercicio: Imprimer la letra "e" mayúscula
letters = {'c1': ['a', 'b', 'c'], 'c2': ['d', 'e', 'f']}
print(letters['c2'][1].upper())

# Modificación
friends = { 'alzate': 'rubio tranquilo de buen corazón', 'peral': 'llanero inteligente y parchado' }
print(f"\nAmigos:\n{friends}")

# Agregando a Jhonsito
friends['jhonsito'] = 'vegano muy atento y sabio'
print(f"\nAmigos con un nuevo amigo:\n{friends}")

# Sobreescribiendo a Peral
friends['peral'] = 'llanero inteligente, parchado y competitivo';
print(f"\nAmigos con datos extra:\n{friends}")

# Metodos utiles

# Obtiene las claves del diccionario
print(friends.keys())
# Obtiene los valores del diccionario
print(friends.values())
#Obtiene tanto claves como valores en tuplas
print(friends.items())