# Creación y tipo
my_set = {1, 1, 1, 3, 1, 2, 5, 6}
print(f"The set type looks like: {type(my_set)}")
print(f"Note the set doesn't repeat any item: {my_set}")

# Debe almacenar datos inmutables
my_loves = set(['Valentina', 'Sara', 'Mariana', 'Sharith', 'Laura'])
#last_loves = set(['Laura', 'Cris', {'name': 'Yuliana'}]) # error porque un diccionario no es inmutable

# Comprobación de valores
valentina_was_a_my_love = 'Valentina' in my_loves
print(f"Valentina is in my loves list? {valentina_was_a_my_love}")

# Union
pets = {'Paco', 'Pepito'}
dead_pets = {'Pepito', 'Sultan', 'Kira'}
all_pets = pets.union(dead_pets)
print(f"All my pets are: {all_pets}")
