mascotas = ["Pelusa", "Pulga", "Felipe", "Chanchito"]


for mascota in enumerate(mascotas):
    # mascota => (0,"Pelusa") => Tupla => se comporta como array de 2 de length
    indice, nombre = mascota
    print(indice, nombre)
