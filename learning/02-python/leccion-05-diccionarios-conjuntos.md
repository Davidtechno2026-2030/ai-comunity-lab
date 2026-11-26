# Lección 05 - Diccionarios y conjuntos

## 1. ¿Qué son los diccionarios?

Los diccionarios permiten almacenar información mediante claves y valores.

Se escriben utilizando llaves {}.

Ejemplo:

    usuario = {
        "nombre": "David",
        "proyecto": "AI Community Lab",
        "version": 0.4
    }

    print(usuario)

## 2. Acceder a los valores

Podemos consultar un valor utilizando su clave.

Ejemplo:

    print(usuario["nombre"])
    print(usuario["proyecto"])

## 3. Modificar valores

Podemos cambiar un valor utilizando su clave.

Ejemplo:

    usuario["version"] = 0.5

    print(usuario)

## 4. Añadir nuevos datos

Podemos añadir nuevas claves y valores.

Ejemplo:

    usuario["lenguaje"] = "Python"

    print(usuario)

## 5. ¿Qué son los conjuntos?

Los conjuntos, llamados sets, almacenan elementos únicos.

Se escriben utilizando llaves {}.

Ejemplo:

    lenguajes = {"Python", "Java", "C++"}

    print(lenguajes)

## 6. Elementos únicos

Los conjuntos eliminan automáticamente los elementos duplicados.

Ejemplo:

    numeros = {1, 2, 2, 3, 3, 4}

    print(numeros)

## 7. Añadir y eliminar elementos

Podemos utilizar add() para añadir elementos y remove() para eliminarlos.

Ejemplo:

    lenguajes = {"Python", "Java"}

    lenguajes.add("C++")
    lenguajes.remove("Java")

    print(lenguajes)

## 8. Diferencias entre diccionarios y conjuntos

- Los diccionarios almacenan claves y valores.
- Los conjuntos almacenan elementos únicos.
- Los diccionarios permiten consultar valores mediante sus claves.
- Los conjuntos no permiten acceder a sus elementos mediante índices.

## Resumen

Los diccionarios permiten organizar información mediante claves y valores.

Los conjuntos permiten almacenar elementos sin duplicados.
