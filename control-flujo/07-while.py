# numero = 1

# while numero < 10:
#     print(numero)
#     numero += 1

# comando = ""

# while comando.lower() != "salir":
#     comando = input("$ ")
#     print(comando)


while True:
    comando = input("$ ")
    print(comando)
    if comando.lower() == "salir":
        break
