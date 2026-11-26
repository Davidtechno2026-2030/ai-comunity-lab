# Ejercicio 05 - Diccionarios y conjuntos

## 1. Crear un diccionario

    usuario = {
        "nombre": "David",
        "proyecto": "AI Community Lab",
        "version": 0.4
    }

    print(usuario)

## 2. Acceder a los valores

    print(usuario["nombre"])
    print(usuario["proyecto"])
    print(usuario["version"])

## 3. Modificar valores

    usuario["version"] = 0.5

    print(usuario)

## 4. Añadir nuevos datos

    usuario["lenguaje"] = "Python"

    print(usuario)

## 5. Crear un conjunto

    lenguajes = {"Python", "Java", "C++"}

    print(lenguajes)
    print(type(lenguajes))

## 6. Eliminar duplicados

    numeros = {1, 2, 2, 3, 3, 4, 4, 5}

    print(numeros)
    print(len(numeros))

## 7. Añadir y eliminar elementos

    lenguajes = {"Python", "Java"}

    lenguajes.add("C++")
    lenguajes.remove("Java")

    print(lenguajes)

## 8. Comparar diccionarios y conjuntos

    usuario = {
        "nombre": "David",
        "lenguaje": "Python"
    }

    lenguajes = {"Python", "Java", "C++"}

    print(type(usuario))
    print(type(lenguajes))

## Conclusión

Los diccionarios (dict) almacenan información mediante claves y valores.

Los conjuntos (set) almacenan elementos únicos y eliminan duplicados.

Ejercicio 05 completado.
