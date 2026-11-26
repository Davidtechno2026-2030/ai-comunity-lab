# Lección 09 - Archivos y lectura de datos

## 1. ¿Qué es un archivo?

Un archivo permite guardar información para utilizarla posteriormente.

Python puede crear, leer y modificar archivos.

## 2. Abrir archivos con open()

La función open() permite abrir un archivo.

Ejemplo:

    archivo = open("datos.txt", "r")

El segundo parámetro indica el modo de apertura.

## 3. Modos de apertura

Los modos principales son:

- "r": leer un archivo.
- "w": escribir y reemplazar su contenido.
- "a": añadir contenido al final.
- "x": crear un archivo nuevo.

## 4. Leer archivos con read()

El método read() permite leer el contenido completo de un archivo.

Ejemplo:

    archivo = open("datos.txt", "r")
    contenido = archivo.read()

    print(contenido)

    archivo.close()

## 5. Escribir archivos con write()

El método write() permite escribir información en un archivo.

Ejemplo:

    archivo = open("datos.txt", "w")

    archivo.write("Bienvenido a AI Community Lab")

    archivo.close()

El modo "w" reemplaza el contenido anterior si el archivo ya existe.

## 6. Añadir contenido con append

El modo "a" permite añadir información sin borrar el contenido anterior.

Ejemplo:

    archivo = open("datos.txt", "a")

    archivo.write("\nNueva información")

    archivo.close()

## 7. Cerrar archivos

El método close() permite cerrar un archivo después de utilizarlo.

Es importante cerrar los archivos para liberar recursos.

## 8. Utilizar with open()

La instrucción with permite gestionar archivos de forma automática.

Ejemplo:

    with open("datos.txt", "r") as archivo:
        contenido = archivo.read()
        print(contenido)

El archivo se cierra automáticamente al terminar el bloque.

## 9. Importancia de trabajar con archivos

Los archivos permiten:

- Guardar información.
- Leer datos posteriormente.
- Mantener registros.
- Almacenar configuraciones.
- Crear programas que conservan información.

## Resumen

open() permite abrir archivos.

read() permite leer información.

write() permite escribir información.

El modo "a" permite añadir contenido.

with open() gestiona el cierre automático del archivo.
