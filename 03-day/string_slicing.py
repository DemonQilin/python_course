"""
Se puede acceder a los caracteres particulares de un string, mediante su indice y la notación de corchetes.
my_text[3] => accediendo al caracter ubicado en el indice 3 (el cuarto)

Para abstraer sub-string de un string se utiliza tambien la notacion de corchetes, con dos numeros, un tercero opcional,
separados por dos puntos.

- El primero indica el indice desde donde comienza la fragmentación, lo incluye. Si no se pasa se asume 0 (inicio)
- El segundo indica el indice donde termina la fragmentación, no lo incluye. Si no se pasa se asume la longitud (final)
- El tercero indica cada cuanto se debe tomar un caracter en el proceso de fragmentado. Con indices negativos se hace al
  reves pero tambien deben invertirse los indices de comienza y final.

Metodo len()
Sirve para obtener la longitud de un string
"""
my_text = "ABCDEFGHIJKL"

from_c_until_f = my_text[2:6]
print(from_c_until_f)

from_a_until_d = my_text[:4]
print(from_a_until_d)

from_h_until_l = my_text[7:]
print(from_h_until_l)

bdf = my_text[1:6:2]
print(bdf)

inverse_abc = my_text[::-1]
print(inverse_abc)

kgc = my_text[-2:1:-4]
print(kgc)
