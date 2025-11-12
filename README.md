# Gestión de Videojuegos

## Descripción

Aplicación en Python para gestionar un catálogo de videojuegos: altas, lecturas, actualizaciones, eliminaciones, búsquedas y estadísticas básicas. Está pensada como proyecto docente/práctico.

## Contenido del repositorio

- [main.py](main.py) — Punto de entrada del programa.
- [U4P09-Gestión de videojuegos.pdf](U4P09-Gestión de videojuegos.pdf) — Enunciado / documentación del ejercicio.
- [src/gestor/**init**.py](src/gestor/__init__.py)

Módulos principales (lógica)

- [src/gestor/catalogo.py](src/gestor/catalogo.py) — Interfaz de consola para operaciones CRUD. Funciones:
  - [`catalogo.añadir_videojuego`](src/gestor/catalogo.py)
  - [`catalogo.actualizar_videojuego`](src/gestor/catalogo.py)
  - [`catalogo.eliminar_videojuego`](src/gestor/catalogo.py)
- [src/gestor/busquedas.py](src/gestor/busquedas.py) — Menú de búsqueda por título, género o rango de años:
  - [`busquedas.menu_busquedas`](src/gestor/busquedas.py)
- [src/gestor/estadisticas.py](src/gestor/estadisticas.py) — Muestra estadísticas del catálogo:
  - [`estadisticas.mostrar_estadisticas`](src/gestor/estadisticas.py)

Almacenamiento y utilidades

- [src/gestor/etapas/diccionarios.py](src/gestor/etapas/diccionarios.py) — Implementación del catálogo (diccionario) y operaciones de negocio:
  - [`diccionarios.crear`](src/gestor/etapas/diccionarios.py)
  - [`diccionarios.leer`](src/gestor/etapas/diccionarios.py)
  - [`diccionarios.actualizar`](src/gestor/etapas/diccionarios.py)
  - [`diccionarios.eliminar`](src/gestor/etapas/diccionarios.py)
  - [`diccionarios.buscar_exacta`](src/gestor/etapas/diccionarios.py)
  - [`diccionarios.buscar_parcial`](src/gestor/etapas/diccionarios.py)
  - [`diccionarios.buscar_por_genero`](src/gestor/etapas/diccionarios.py)
  - [`diccionarios.buscar_por_rango_anios`](src/gestor/etapas/diccionarios.py)
  - [`diccionarios.estadisticas`](src/gestor/etapas/diccionarios.py)
- Scripts de ejemplo educativos en [src/gestor/etapas/](src/gestor/etapas/):
  - [cadenas.py](src/gestor/etapas/cadenas.py)
  - [listas.py](src/gestor/etapas/listas.py)
  - [conjuntos.py](src/gestor/etapas/conjuntos.py)
  - [tuplas.py](src/gestor/etapas/tuplas.py)

## Instalación

1. Clonar el repositorio.
2. (Opcional) Crear y activar un entorno virtual.
3. Ejecutar:

```sh
python main.py
```

## Uso

Al ejecutar [main.py](main.py) se mostrará un menú con opciones para añadir, actualizar, eliminar, buscar y ver estadísticas. El flujo de entrada/ salida se hace por consola.

## Formato de datos del catálogo

El catálogo interno (en [src/gestor/etapas/diccionarios.py](src/gestor/etapas/diccionarios.py)) usa claves normalizadas y valores con la forma:
{
"clave_normalizada": {
"titulo": "Título original",
"anio": 2011,
"genero": set([...])
}
}

## Buenas prácticas y mejoras sugeridas

- Añadir persistencia en disco (JSON, SQLite).
- Validación robusta de entradas (año, género).
- Internacionalización / normalización de acentos.
- Reemplazar inputs bloqueantes por interfaz gráfica o web si se desea.

## Contribuir

1. Fork
2. Branch por feature
3. Pull request con descripción de cambios

## Colaboradores

<table>
  <tr>
    <td align="center"><img src="https://github.com/said-oudrhich.png" width="80" /></td>
    <td align="center"><img src="https://github.com/Cesarymarco.png" width="80" /></td>
    <td align="center"><img src="https://github.com/MGSM05.png" width="80" /></td>
    <td align="center"><img src="https://github.com/danielgmdaw-glitch.png" width="80" /></td>
  </tr>
  <tr>
    <td align="center"><b>@said-oudrhich</b><br>Said Oudrhich Soukrati</td>
    <td align="center"><b>@Cesarymarco</b><br>César Sánchez Martín</td>
    <td align="center"><b>@MGSM05</b><br>Mario Gonzalez San Martin</td>
    <td align="center"><b>@danielgmdaw-glitch</b><br>Daniel García Mora</td>
  </tr>
</table>

## Archivos en el workspace (rápido acceso)

- [main.py](main.py)
- [README.md](README.md)
- [U4P09-Gestión de videojuegos.pdf](U4P09-Gestión de videojuegos.pdf)
- [src/gestor/**init**.py](src/gestor/__init__.py)
- [src/gestor/busquedas.py](src/gestor/busquedas.py)
- [src/gestor/catalogo.py](src/gestor/catalogo.py)
- [src/gestor/estadisticas.py](src/gestor/estadisticas.py)
- [src/gestor/utils_texto.py](src/gestor/utils_texto.py)
- [src/gestor/etapas/cadenas.py](src/gestor/etapas/cadenas.py)
- [src/gestor/etapas/conjuntos.py](src/gestor/etapas/conjuntos.py)
- [src/gestor/etapas/diccionarios.py](src/gestor/etapas/diccionarios.py)
- [src/gestor/etapas/listas.py](src/gestor/etapas/listas.py)
- [src/gestor/etapas/tuplas.py](src/gestor/etapas/tuplas.py)
