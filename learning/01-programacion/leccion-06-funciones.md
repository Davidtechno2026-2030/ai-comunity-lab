# Lección 06 - Funciones

## 1. ¿Qué es una función?

Una función es un bloque de código que realiza una tarea concreta y que podemos reutilizar cuando lo necesitemos.

## 2. Crear una función

En Python utilizamos la palabra def para crear una función.

Ejemplo:

    def saludar():
        print("Hola, bienvenido a AI Community Lab")

## 3. Ejecutar una función

Para ejecutar una función escribimos su nombre seguido de paréntesis.

    saludar()

## 4. Funciones con parámetros

Una función puede recibir información mediante parámetros.

Ejemplo:

    def saludar(nombre):
        print("Hola", nombre)

    saludar("Ana")

## 5. Funciones con return

La instrucción return permite devolver un resultado.

Ejemplo:

    def sumar(numero_a, numero_b):
        return numero_a + numero_b

    resultado = sumar(5, 3)
    print(resultado)

Resultado:

    8

## 6. Ventajas de las funciones

- Permiten reutilizar código.
- Organizan mejor los programas.
- Evitan repetir instrucciones.
- Facilitan el mantenimiento del código.

## Resumen

Las funciones permiten dividir un programa en bloques pequeños, organizados y reutilizables.
