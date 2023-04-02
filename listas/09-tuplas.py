# las tuplas no son mutables

numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

# crear tupla a partir de un iterable
punto = tuple([1, 2])
print(punto)

menosNumeros = numeros[:2]
print(menosNumeros)
primero, segundo, *otros = numeros
print(primero, segundo, otros)
