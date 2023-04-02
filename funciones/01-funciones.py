def saludar(nombre, apellido="Sin apellido"):
    print("hola", nombre, apellido)


saludar("Stefano", "Gemelli")
saludar("Stefano")
saludar(apellido="Gemelli", nombre="Stefano")  # argumentos nombrados
