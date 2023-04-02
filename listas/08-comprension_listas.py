usuarios = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5],
]

# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[1])
# print(nombres)

# nombres = [usuario[0] for usuario in usuarios]  # mapeo

# filtrado
# nombres = [usuario for usuario in usuarios if usuario[1] > 2]
# nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]

# map
# nombres = list(map(lambda usuario: usuario[0], usuarios))

# filter
menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios)
