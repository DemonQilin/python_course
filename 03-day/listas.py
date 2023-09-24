"""
Listas <list>
Las listas son secuencias ordenadas de datos, que pueden ser de varios tipos. Se puede acceder a sus elementos con la
notación de corchetes y en cuanto a esto y fragmentación funciona igual que los string.

A diferencia de los string, las listas son mutables, se pueden reasignar sus elementos, agregar y eliminar.

- append(element): Agregar un elemento al final de la lista
- pop: elimina un elemento de la lista dado el indice y lo retorna, por defecto elimina el último
"""

list_1 = ["Python", "Javascript", "Rust"]
list_2 = ["Golang", "Haskell", "PHP"]
list_3 = list_1 + list_2

list_3[2] = "Zig"
list_1.append("Zig")
list_2.pop()

print(list_1)
print(list_2)
print(list_3)