#Listar, buscar, filtrar, añadir, actualizar y eliminar videojuegos.
#Mostrar estadísticas generales.


from src.gestor import catalogo, busquedas, estadisticas


if __name__ == "__main__":
    opcion = 0
    while opcion != 6:
        print ("1: Añadir nuevo videojuego")
        print ("2: Actualizar videojuegos")
        print ("3: Eliminar videojuego")
        print ("4: Buscar videojuegos")
        print ("5: Mostrar estadisticas videojuego")
        print ("6: Salir")

        opcion = int(input("Seleccione una opción: "))

        match opcion:
            case 1:
                catalogo.añadir_videojuego()
            case 2:
                catalogo.actualizar_videojuego()
            case 3:
                catalogo.eliminar_videojuego()
            case 4:
                busquedas.menu_busquedas()
            case 5:
                estadisticas.mostrar_estadisticas()
            case 6:
                print("Saliendo...")
                