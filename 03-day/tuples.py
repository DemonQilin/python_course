# Creación y tipo
my_tuple = (1, 2, 3, 4)
print(f"Tuple type looks like: {type(my_tuple)}")

# Lectura
friends = 'Alzatico', 'Peral', 'Jhonsito' # Se pueden crear sin parentesis
print(f"My best friend is {friends[0]}")

# Tuplas con valores compuestos
debtors = ({'name': 'Susana', 'money': 300}, {'name': 'Sharith', 'money': 3200}, {'name': 'Alzatico', 'money': 500})
print(f"The largest debtor is {debtors[1]['name']} with {debtors[1]['money']} thousand pesos")

# Casting
debtors = list(debtors)
debtors = tuple(debtors)

# Unpacking
letters = ('a', 'b', 'c', 'd')
print(f"The tuple is: {letters}")

# p1, p2 = letters # Menos elementos lanza error
# p1, p2, p3, p4, p5 = letters # Más elementos lanza error
p1,p2,p3,p4 = letters
print(f"p1: {p1}, p2: {p2}, p3: {p3}, p4: {p4}")

# Utilidades
numbers = 1,2,3,4,2,1,2,2
print(f"The numbers are: {numbers}")

total_two = numbers.count(2)
print(f"2 appears {total_two} times in numbers")
