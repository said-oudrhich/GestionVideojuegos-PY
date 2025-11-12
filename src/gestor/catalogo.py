

from src.gestor.etapas import diccionarios


def añadir_videojuego():
    titulo = input("Ingrese el título del videojuego: ")
    genero = input("Ingrese el género del videojuego: ")
    año = int(input("Ingrese el año de lanzamiento del videojuego: "))
    diccionarios.crear(titulo, año, genero)

def actualizar_videojuego():
    titulo = input("Ingrese el título del videojuego a actualizar: ")
    diccionarios.actualizar(titulo)

def eliminar_videojuego():
    titulo = input("Ingrese el título del videojuego a eliminar: ")
    diccionarios.eliminar(titulo)

