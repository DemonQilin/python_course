"""
Al igual que en Javascript en los string cada caracter tiene un numero de indice que comienza de cero y aumenta de
izquierda a derecha. Tambien existen indices negativos, que van de derecha a izquierda y comienzan con la ultima letra
siendo el -1.

Metodo "index"
Busca el sub-string que se le pasa como primer parametro dentro del string desde donde se llama. Siempre busca de izquierda
a derecha y trae el indice desde donde comienza la coincidencia. La busqueda es sensible a mayusculas.

Si no encuentra una coincidencia para el sub-string recibido, lanza un error.

Tambien recibe dos paremtros adicionales:
- start: indice del string desde donde comienza la busqueda.
- end: indice hasta donde llega la busquda pero no lo incluye dentro de la busqueda.

Existe su contra parte que busca de derecha a izquierda y se llama rindex.
"""
mi_texto = "Esta es una prueba"

index_n = mi_texto.index("n")
print(index_n)

index_first_a = mi_texto.index("a")
print(index_first_a)

index_second_a = mi_texto.index("a", 4)
print(index_second_a)

# index_error = mi_texto.index("x")

index_last_a = mi_texto.rindex("a")
print(index_last_a)
