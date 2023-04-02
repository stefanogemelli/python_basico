numeros = [1, 2, 3, 4, 5, 6, 7]


# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

# primero, segundo, tercero = numeros
primero, *otros, ultimo = numeros

print(primero)
print(otros)
print(ultimo)
