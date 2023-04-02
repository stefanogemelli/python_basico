primero = {1, 2, 3, 4, 5, 2, 2, 3, 4, 4, 4}
empanadas = {
    "choclo",
    "carne",
    "verdura",
    "pescado",
    "choclo",
    "carne",
    "choclo",
    "carne",
    "choclo",
    "choclo",
    "choclo"
}
segundo = [4, 5, 5, 5, 5, 6]
segundo = set(segundo)
print(primero | segundo)  # union
print(primero & segundo)  # interseccion
print(primero - segundo)  # diferencia
print(primero ^ segundo)  # diferencia simétrica (retorna los que no se repiten)

# no se puede acceder a indices de la forma => primero[0] !==
if 5 in segundo:
    print("Hola mundo")
