
from src.gestor.etapas import diccionarios


def menu_busquedas():
    print ("1: Buscar por título")
    print ("2: Buscar por género")
    print ("3: Buscar por rango de años")

    opcion = int(input("Seleccione una opción: "))

    match opcion:
        case 1:
            titulo = input("Ingrese el título del videojuego: ")
            diccionarios.buscar_exacta(titulo)
        case 2:
            genero = input("Ingrese el género del videojuego: ")
            diccionarios.buscar_por_genero(genero)
        case 3:
            año_inicio = int(input("Ingrese el año de inicio: "))
            año_fin = int(input("Ingrese el año de fin: "))
            diccionarios.buscar_por_rango_anios(año_inicio, año_fin)
        

