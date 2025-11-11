# Crear una lista con titulos videojuegos
videojuegos = ["Minecraft",
               "God of War",
               "Dark Souls III",
               "Clash Royale",
               "Elden Ring"]

# Añadir nuevos videojuegos al final de la lista
videojuegos.append("Fortnite")
videojuegos.append("Cyberpunk 2077")

# Insertar un videojuego en una posicion especifica 
videojuegos.insert(2, "Super Mario Bros")

# Eliminar un videojuego de la lista
videojuegos.remove("Cyberpunk 2077")

# Recorrer la lista e imprimir los titulos numerados
print("LISTA DE VIDEOJUEGOS: ")
for i, juego in enumerate(videojuegos, start=1):
    print(f"{i}. {juego}")

# Mostrar la lista ordenada alfabeticamente
print("\nLISTA ORDENADA ALFABETICAMENTE: ")
for i, juego in enumerate(sorted(videojuegos), start=1):
    print(f"{i}. {juego}")