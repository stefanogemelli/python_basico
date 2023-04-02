numeros = [15, 5, 7, 1, 4, 2]

# numeros.sort(reverse=True)
numeros2 = sorted(numeros, reverse=True)  # sorted no muta la lista

print(numeros)
print(numeros2)


usuarios = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5],
]


def ordena(elemento):
    return elemento[1]


# usuarios.sort(key=ordena, reverse=True)
# usuarios.sort(key=lambda el: el[1], reverse=True)
usuarios.sort(key=lambda el: el[1])

print(usuarios)
