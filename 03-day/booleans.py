# Creación directa y tipo
is_true = True
is_false = False
print(f"Boolean type loooks like: {type(is_true)}")
print(f"true: {is_true}, false: {is_false}")

# Creación con expresiones
is_greather = 5 > 2+3
print(f"5 > 2 + 3: {is_greather}")

is_equal = 5 == 2 + 3
print(f"5 == 2 + 3: {is_equal}")

# Verificaciones
my_list = [1, 2, 3, 4]
control = 5 in my_list
print(f"5 in {my_list}? {control}")
