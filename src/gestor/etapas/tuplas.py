# Lista de videojuegos representados como tuplas (título, año, género)
videojuegos = [
    ("The Legend of Zelda", 1986, "Rol"),
    ("Super Mario Bros", 1985, "Plataformas"),
    ("Minecraft", 2011, "Construcción"),
    ("The Witcher 3: Wild Hunt", 2015, "Rol"),
    ("God of War", 2018, "Acción")
]

# Recorremos la lista e imprimimos los datos con el formato indicado
for titulo, año, genero in videojuegos:
    print(f"{titulo} ({año}) {genero}")
