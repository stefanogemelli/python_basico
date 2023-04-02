animal = "  Chancho feliz "
print(animal.upper())
print(animal.lower())
print(animal.strip().capitalize())    # strip => trim
print(animal.title())
print(animal.strip())   # trim
print(animal.lstrip())   # left trim
print(animal.rstrip())   # right trim
print(animal.replace("ch", "Hola"))
print(animal.find("ch"))
print("ch" in animal)   # => True / False
print("ch" not in animal)
