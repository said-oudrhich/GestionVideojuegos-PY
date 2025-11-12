# Lista de videojuegos como tuplas (título, año, género)
videojuegos = [
    ("The Legend of Zelda", 1986, "Rol"),
    ("Super Mario Bros", 1985, "Plataformas"),
    ("Minecraft", 2011, "Construcción"),
    ("The Witcher 3: Wild Hunt", 2015, "Rol"),
    ("God of War", 2018, "Acción")
]

# Pedimos el nombre del videojuego al usuario
nombre = input("Escribe el nombre de un videojuego: ")

# # Quitamos espacios y pasamos a minúsculas para comparar
nombre_juego = nombre.strip().lower().replace("  ", " ")

# Buscamos si existe en la lista (ignorando mayúsculas y espacios)
encontrado = False
for titulo, año, genero in videojuegos:
    if titulo.lower().strip() == nombre_juego:
        print(f"Título: {titulo} | Género: {genero} | Año: {año}")
        encontrado = True
        break

# Si no se encontró
if not encontrado:
    print("El videojuego no se encuentra en la lista.")
