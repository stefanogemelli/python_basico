lista1 = [1, 2, 3, 4]
# print(*lista)
lista2 = [5, 6, 7]

# exactamente igual que el rest(...) de js
listaCombinada = [*lista1, *lista2]

print(listaCombinada)


# en diccionarios se usa **
punto1 = {"x": 19}
punto2 = {"y": 15}

nuevoPunto = {**punto1, **punto2}
print(nuevoPunto)
