# Ejercicio 06 - Cadenas de texto

## 1. Crear cadenas de texto

    nombre = "David"
    proyecto = "AI Community Lab"

    print(nombre)
    print(proyecto)
    print(type(nombre))

## 2. Contar caracteres

    mensaje = "AI Community Lab"

    print(len(mensaje))

## 3. Convertir a mayúsculas

    mensaje = "ai community lab"

    resultado = mensaje.upper()

    print(resultado)

## 4. Convertir a minúsculas

    mensaje = "AI COMMUNITY LAB"

    resultado = mensaje.lower()

    print(resultado)

## 5. Reemplazar palabras

    mensaje = "Estoy aprendiendo Java"

    resultado = mensaje.replace("Java", "Python")

    print(resultado)

## 6. Separar texto

    tecnologias = "Python Java HTML CSS"

    resultado = tecnologias.split()

    print(resultado)
    print(type(resultado))

## 7. Combinar texto con f-strings

    nombre = "David"
    proyecto = "AI Community Lab"
    version = 0.5

    mensaje = f"{nombre} está desarrollando {proyecto}, versión {version}"

    print(mensaje)

## 8. Eliminar espacios exteriores

    mensaje = "   Hola Python   "

    resultado = mensaje.strip()

    print(resultado)
    print(len(mensaje))
    print(len(resultado))

## Conclusión

Las cadenas de texto (str) permiten almacenar y manipular información escrita.

Python ofrece diferentes funciones y métodos para transformar, separar, combinar y limpiar textos.

Ejercicio 06 completado.
