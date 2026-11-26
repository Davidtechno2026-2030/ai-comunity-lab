# Lección 04 - Listas y tuplas

## 1. ¿Qué son las listas?

Las listas permiten almacenar varios elementos dentro de una misma variable.

Se escriben utilizando corchetes [].

Ejemplo:

    lenguajes = ["Python", "Java", "JavaScript"]
    print(lenguajes)

## 2. Acceder a los elementos

Cada elemento tiene una posición llamada índice.

Python comienza a contar desde 0.

Ejemplo:

    lenguajes = ["Python", "Java", "JavaScript"]

    print(lenguajes[0])
    print(lenguajes[1])
    print(lenguajes[2])

## 3. Modificar elementos

Podemos cambiar un elemento utilizando su índice.

Ejemplo:

    lenguajes = ["Python", "Java", "JavaScript"]

    lenguajes[1] = "C++"

    print(lenguajes)

## 4. Añadir elementos

El método append() permite añadir elementos al final de una lista.

Ejemplo:

    lenguajes = ["Python", "Java"]

    lenguajes.append("JavaScript")

    print(lenguajes)

## 5. Eliminar elementos

El método remove() permite eliminar un elemento por su valor.

Ejemplo:

    lenguajes = ["Python", "Java", "C++"]

    lenguajes.remove("Java")

    print(lenguajes)

## 6. ¿Qué son las tuplas?

Las tuplas permiten almacenar varios elementos, igual que las listas.

Se escriben utilizando paréntesis ().

Ejemplo:

    coordenadas = (10, 20)

    print(coordenadas)

## 7. Diferencias entre listas y tuplas

- Las listas pueden modificarse.
- Las tuplas no pueden modificarse después de crearse.
- Las listas utilizan corchetes [].
- Las tuplas utilizan paréntesis ().

## Resumen

Las listas y las tuplas permiten organizar varios datos dentro de una variable.

Las listas son modificables, mientras que las tuplas son inmutables.
