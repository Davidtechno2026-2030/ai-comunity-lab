# Lección 08 - Manejo de errores

## 1. ¿Qué son los errores?

Los errores son problemas que aparecen cuando un programa intenta ejecutar una operación que no puede realizar.

En Python se conocen como excepciones.

## 2. Bloque try

La instrucción try permite ejecutar código que podría producir un error.

Ejemplo:

    try:
        numero = int("25")
        print(numero)
    except ValueError:
        print("Ha ocurrido un error")

## 3. Bloque except

La instrucción except permite controlar un error y ejecutar una respuesta alternativa.

Ejemplo:

    try:
        numero = int("hola")
    except ValueError:
        print("No se puede convertir ese texto en número")

## 4. Controlar divisiones entre cero

Python genera un error cuando intentamos dividir un número entre cero.

Podemos controlar esa situación:

    try:
        resultado = 10 / 0
        print(resultado)
    except ZeroDivisionError:
        print("No se puede dividir entre cero")

## 5. Bloque finally

La instrucción finally permite ejecutar código al finalizar el bloque try, haya ocurrido un error o no.

Ejemplo:

    try:
        print("Ejecutando programa")
    except ValueError:
        print("Error detectado")
    finally:
        print("Programa finalizado")

## 6. Varios tipos de errores

Podemos controlar diferentes excepciones utilizando varios bloques except.

Ejemplo:

    try:
        numero = int("hola")
        resultado = 10 / numero
    except ValueError:
        print("Error: valor no válido")
    except ZeroDivisionError:
        print("Error: división entre cero")

## 7. Importancia del manejo de errores

El manejo de errores permite:

- Evitar interrupciones inesperadas.
- Mostrar mensajes comprensibles.
- Controlar situaciones problemáticas.
- Crear programas más robustos.

## Resumen

try permite ejecutar código que podría producir errores.

except permite controlar las excepciones.

finally ejecuta instrucciones al finalizar el bloque.

El manejo de errores ayuda a crear programas más estables.
