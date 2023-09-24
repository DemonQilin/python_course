"""
Función round
Python incorpora una función llamada "round" que recibe dos parametros: el primero el numero a redondear
y el segundo la cantidad de decimales a la que se desea redondear.

En general, es importante tener en cuenta que la función round tiene algunas
limitaciones y comportamientos inesperados en ciertos casos de borde.
Si se necesita una muy buena precisión al redondear números, es recomendable utilizar bibliotecas especializadas
como decimal o numpy.

- Rounding a 0.5: Cuando se redondea un número que termina en 0.5, la función round lo redondeará al número par más cercano.
Para evitar este comportamiento, una solución es utilizar la función decimal y redondear utilizando la regla de redondeo
 de "redondear hacia arriba si el dígito siguiente es >=5" o "redondear hacia abajo si el dígito siguiente es <5".

- Rounding with negative numbers: Si se redondea un número negativo con un número impar de decimales, el resultado puede
ser diferente de lo esperado. Por ejemplo, round(-2.5, 1) devuelve -2.4, en lugar de -2.5. Para evitar este
comportamiento, una solución es utilizar la función decimal y redondear utilizando la regla de redondeo de
"redondear hacia arriba si el dígito siguiente es >=5" o "redondear hacia abajo si el dígito siguiente es <5".

- Cuando no se pasa el segundo parametros, se establece por defecto a cero, y ademas se hace un casting implicito del
resultado a <int>. Si en comparación se pasara 0 explicitamente, no se hace el casting.
"""
price = 97
friends = 9
total = 97/9

print(f"El resultado redondeado a entero es {round(price/friends)}")
print(f"El resultado redondeado a centavos es {round(price/friends, 3)}")
