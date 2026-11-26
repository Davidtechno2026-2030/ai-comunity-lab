# Lección 06 - Cadenas de texto

## 1. ¿Qué son las cadenas de texto?

Las cadenas de texto, llamadas strings, permiten almacenar palabras, frases y caracteres.

Se escriben entre comillas simples o dobles.

Ejemplo:

    nombre = "David"
    proyecto = "AI Community Lab"

    print(nombre)
    print(proyecto)

## 2. Conocer la longitud de un texto

La función len() permite contar los caracteres de una cadena.

Ejemplo:

    mensaje = "Hola Python"

    print(len(mensaje))

## 3. Convertir texto a mayúsculas

El método upper() convierte todos los caracteres a mayúsculas.

Ejemplo:

    mensaje = "hola python"

    print(mensaje.upper())

## 4. Convertir texto a minúsculas

El método lower() convierte todos los caracteres a minúsculas.

Ejemplo:

    mensaje = "HOLA PYTHON"

    print(mensaje.lower())

## 5. Reemplazar palabras

El método replace() permite sustituir una parte del texto por otra.

Ejemplo:

    mensaje = "Estoy aprendiendo Java"

    nuevo_mensaje = mensaje.replace("Java", "Python")

    print(nuevo_mensaje)

## 6. Separar cadenas de texto

El método split() divide una cadena en una lista de elementos.

Por defecto, utiliza los espacios como separadores.

Ejemplo:

    tecnologias = "Python Java HTML CSS"

    resultado = tecnologias.split()

    print(resultado)

## 7. Combinar texto con f-strings

Las f-strings permiten insertar variables dentro de una cadena de texto.

Se escriben colocando la letra f delante de las comillas.

Ejemplo:

    nombre = "David"
    proyecto = "AI Community Lab"

    mensaje = f"{nombre} está desarrollando {proyecto}"

    print(mensaje)

## 8. Eliminar espacios exteriores

El método strip() elimina los espacios al principio y al final de una cadena.

Ejemplo:

    mensaje = "   Hola Python   "

    print(mensaje.strip())

## Resumen

Las cadenas de texto permiten trabajar con información escrita.

Python ofrece métodos como len(), upper(), lower(), replace(), split() y strip() para manipularlas.
