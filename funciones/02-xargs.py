def suma(*numeros):     # el * es como el ... de js
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2, 3)
suma(1, 2, 3, 4, 2, 1, 2, 12)
