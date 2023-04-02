
# range(5) => 0,1,2,3,4
# range(5,7) => 5,6

buscar = 3
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
else:
    print("numero no encontrado")

# el else solo se ejecuta si no se ejecuta el break del for


for char in "Stefano":
    print(char)
