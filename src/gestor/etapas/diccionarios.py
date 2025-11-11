def normalizar_titulo(titulo):
    return titulo.strip().lower().replace(" ", "_")

catalogo = {
    normalizar_titulo("Minecraft"): {"titulo": "Minecraft", "anio": 2011, "genero": {"Sandbox", "Supervivencia"}},
    normalizar_titulo("God of War"): {"titulo": "God of War", "anio": 2018, "genero": {"Accion", "Aventura"}},
    normalizar_titulo("Dark Souls III"): {"titulo": "Dark Souls III", "anio": 2016, "genero": {"Rol", "Accion"}},
    normalizar_titulo("Clash Royale"): {"titulo": "Clash Royale", "anio": 2016, "genero": {"Estrategia"}},
    normalizar_titulo("Elden Ring"): {"titulo": "Elden Ring", "anio": 2022, "genero": {"Rol", "Aventura"}}
}

# ==========================

def crear(titulo, anio, genero):
    clave = normalizar_titulo(titulo)
    if clave in catalogo:
        print("El videojuego ya existe.")
    else:
        catalogo[clave] = {"titulo": titulo, "anio": anio, "genero": set(genero)}
        print(f"{titulo} anadido correctamente.")

def leer(titulo):
    clave = normalizar_titulo(titulo)
    j = catalogo.get(clave)
    if j:
        print(f"{j['titulo']} ({j['anio']}) - Genero: {', '.join(j['genero'])}")
    else:
        print("Videojuego no encontrado.")

def actualizar(titulo, anio=None, genero=None):
    clave = normalizar_titulo(titulo)
    j = catalogo.get(clave)
    if j:
        if anio:
            j["anio"] = anio
        if genero:
            j["genero"] = set(genero)
        print(f"{titulo} actualizado correctamente.")
    else:
        print("No se puede actualizar: el videojuego no existe.")

def eliminar(titulo):
    clave = normalizar_titulo(titulo)
    if catalogo.pop(clave, None):
        print(f"{titulo} eliminado del catalogo.")
    else:
        print("El videojuego no existe.")

# ==========================

def buscar_exacta(titulo):
    leer(titulo)

def buscar_parcial(fragmento):
    fragmento = fragmento.lower()
    resultados = [j["titulo"] for j in catalogo.values() if fragmento in j["titulo"].lower()]
    if resultados:
        print("Resultados:", ", ".join(resultados))
    else:
        print("No se encontraron coincidencias.")

def buscar_por_genero(genero):
    genero = genero.capitalize()
    resultados = [j["titulo"] for j in catalogo.values() if genero in j["genero"]]
    if resultados:
        print(f"Videojuegos del genero {genero}:", ", ".join(resultados))
    else:
        print("Ningun videojuego de ese genero encontrado.")

def buscar_por_rango_anios(inicio, fin):
    resultados = [j["titulo"] for j in catalogo.values() if inicio <= j["anio"] <= fin]
    if resultados:
        print(f"Videojuegos entre {inicio} y {fin}:", ", ".join(resultados))
    else:
        print("Ningun videojuego en ese rango de anios.")

# ==========================

def estadisticas():
    total = len(catalogo)
    conteo = {}
    for j in catalogo.values():
        for g in j["genero"]:
            conteo[g] = conteo.get(g, 0) + 1
    print(f"\nTotal de videojuegos: {total}")
    print("Conteo por genero:")
    for g, c in conteo.items():
        print(f" - {g}: {c}")