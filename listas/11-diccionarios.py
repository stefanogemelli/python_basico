punto = {"x": 25, "y": 50}
print(punto)
print(punto["x"])

punto["z"] = 45

# print(punto)
if "abc" in punto:
    print(punto["abc"])


# esta forma retorna None si no encuentra el valor
# 97 es un valor por defecto
print(punto.get("abc", 97))

del punto["x"]
del (punto["y"])

print(punto)

punto["x"] = 25

# este for retorna las keys
for valor in punto:
    print(valor)

# este for retorna tuplas
for valor in punto.items():
    print(valor)

# destructuring
for llave, valor in punto.items():
    print(llave, valor)


usuarios = [
    {"id": 1, "nombre": "Chanchito"},
    {"id": 2, "nombre": "Feliz"},
    {"id": 3, "nombre": "Stefano"},
    {"id": 4, "nombre": "Harold"},
]

for usuario in usuarios:
    print(usuario["nombre"])
