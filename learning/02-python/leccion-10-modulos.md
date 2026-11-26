# Lección 10 - Módulos e importaciones

## 1. ¿Qué son los módulos?

Un módulo es un archivo de Python que contiene código reutilizable.

Puede incluir funciones, variables y clases.

Los módulos permiten organizar programas y reutilizar código.

## 2. Importar módulos con import

La instrucción import permite utilizar módulos existentes.

Ejemplo:

    import math

    resultado = math.sqrt(25)

    print(resultado)

El módulo math proporciona funciones matemáticas.

## 3. Utilizar módulos estándar

Python incluye módulos que podemos utilizar sin instalarlos.

Algunos ejemplos:

- math: operaciones matemáticas.
- random: generación de valores aleatorios.
- os: interacción con el sistema operativo.
- datetime: gestión de fechas y horas.

## 4. Importar funciones concretas

Podemos importar solamente una función de un módulo.

Ejemplo:

    from math import sqrt

    resultado = sqrt(36)

    print(resultado)

## 5. Utilizar alias

Podemos asignar un nombre abreviado a un módulo utilizando as.

Ejemplo:

    import math as m

    print(m.sqrt(49))

## 6. Crear nuestros propios módulos

También podemos crear módulos propios.

Por ejemplo, podemos crear un archivo llamado operaciones.py.

Su contenido:

    def sumar(a, b):
        return a + b

    def restar(a, b):
        return a - b

## 7. Importar nuestros módulos

Si tenemos otro archivo en la misma carpeta, podemos importar nuestro módulo.

Ejemplo:

    import operaciones

    resultado = operaciones.sumar(5, 3)

    print(resultado)

## 8. Ventajas de los módulos

Los módulos permiten:

- Organizar el código.
- Reutilizar funciones.
- Separar responsabilidades.
- Facilitar el mantenimiento.
- Crear proyectos más grandes y ordenados.

## Resumen

import permite importar módulos.

from permite importar elementos concretos.

as permite utilizar alias.

También podemos crear nuestros propios módulos de Python.
