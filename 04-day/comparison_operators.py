# Comparación de igualdad
are_equal = 10 == 25
are_equal = 'blanco' == 'negro'
print(are_equal)

# Comparación de diferencia
are_diferent = 100 != 101
print(are_diferent)

# Diferencia igualdad e identidad
x = [1,2,3]
y = [1,2,3]
is_equal_value = x == y
is_exactly_same_object = x is y

print(f"x = {x} has same content of y = {y} ?: {is_equal_value}")
print(f"x and y are in same memory space?: {is_exactly_same_object}")
