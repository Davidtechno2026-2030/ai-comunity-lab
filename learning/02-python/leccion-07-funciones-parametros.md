# Lección 07 - Funciones y parámetros

## 1. ¿Qué son las funciones?

Las funciones son bloques de código que realizan una tarea concreta.

Permiten organizar y reutilizar código.

Se crean utilizando la palabra reservada def.

Ejemplo:

    def saludar():
        print("Bienvenido a Python")

    saludar()

## 2. Funciones con parámetros

Los parámetros permiten enviar información a una función.

Ejemplo:

    def saludar(nombre):
        print(f"Hola, {nombre}")

    saludar("David")

## 3. Funciones con varios parámetros

Una función puede recibir varios parámetros.

Ejemplo:

    def presentar(nombre, proyecto):
        print(f"{nombre} está desarrollando {proyecto}")

    presentar("David", "AI Community Lab")

## 4. Devolver resultados con return

La instrucción return permite devolver un resultado desde una función.

Ejemplo:

    def sumar(a, b):
        resultado = a + b
        return resultado

    total = sumar(5, 3)

    print(total)

## 5. Parámetros predeterminados

Podemos establecer valores predeterminados para los parámetros.

Se utilizan cuando no proporcionamos un valor al llamar a la función.

Ejemplo:

    def saludar(nombre="Usuario"):
        print(f"Hola, {nombre}")

    saludar()
    saludar("David")

## 6. Reutilizar funciones

Una función puede ejecutarse tantas veces como sea necesario.

Ejemplo:

    def mostrar_proyecto():
        print("AI Community Lab")

    mostrar_proyecto()
    mostrar_proyecto()
    mostrar_proyecto()

## 7. Funciones con condiciones

Las funciones también pueden contener instrucciones condicionales.

Ejemplo:

    def comprobar_numero(numero):
        if numero > 0:
            return "Positivo"
        elif numero < 0:
            return "Negativo"
        else:
            return "Cero"

    print(comprobar_numero(5))
    print(comprobar_numero(-3))
    print(comprobar_numero(0))

## 8. Diferencia entre print() y return

- print() muestra información en pantalla.
- return devuelve un resultado que puede utilizarse posteriormente.
- Una función puede utilizar return para entregar información a otra parte del programa.

Ejemplo:

    def multiplicar(a, b):
        return a * b

    resultado = multiplicar(4, 5)

    print(resultado)

## Resumen

Las funciones permiten dividir un programa en bloques reutilizables.

Los parámetros permiten enviar información y return permite devolver resultados.
