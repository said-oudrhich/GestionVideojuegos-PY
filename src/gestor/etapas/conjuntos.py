
# Conjunto de géneros de nuestros videojuegos
generosJuegos = { "Acción", "Aventura", "Rol", "Estrategia", "Deportes", "Simulación", "Puzzle", "Terror" }

#Añadir nuevos géneros 
generosJuegos.add("Indie")
generosJuegos.add("MMORPG")

#Eliminar generos
generosJuegos.discard("Deportes")
generosJuegos.discard("Terror")

#Preguntar si un género está en el conjunto y comprobarlo
generoPreguntar = str(input("Ingrese un género de videojuego para verificar si está en el conjunto: "))

if generoPreguntar in generosJuegos:
    print(f"El género '{generoPreguntar}' está dentro de los generos de nuestros videojuegos.")
else:
    print(f"El género '{generoPreguntar}' no está dentro de los generos que tienen nuestros videojuegos.")

#Crear y comparar nuevo conjunto con el nuestro
generosAmigo = { "Acción", "Deportes", "Simulación", "Indie", "MMORPG", "Carreras" }

print(f"La union entre los generos de mi amigo y los mios es: {generosJuegos.union(generosAmigo)}")

print(f"La intersección entre los generos de mi amigo y los mios es: {generosJuegos.intersection(generosAmigo)}")

print(f"La diferencia entre los generos de mi amigo y los mios es: {generosJuegos.difference(generosAmigo)}")
