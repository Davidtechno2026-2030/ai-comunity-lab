# Lección 03 - Operadores y expresiones

## 1. ¿Qué son los operadores?

Los operadores permiten realizar operaciones con datos y variables.

Python dispone de operadores aritméticos, de comparación y lógicos.

## 2. Operadores aritméticos

Se utilizan para realizar cálculos matemáticos.

- + : suma.
- - : resta.
- * : multiplicación.
- / : división.
- // : división entera.
- % : resto de una división.
- ** : potencia.

Ejemplo:

    numero1 = 10
    numero2 = 5

    print(numero1 + numero2)
    print(numero1 - numero2)
    print(numero1 * numero2)
    print(numero1 / numero2)

## 3. Operadores de comparación

Permiten comparar dos valores.

- == : igual que.
- != : diferente de.
- > : mayor que.
- < : menor que.
- >= : mayor o igual que.
- <= : menor o igual que.

El resultado de una comparación es un valor booleano: True o False.

Ejemplo:

    edad = 18

    print(edad >= 18)
    print(edad == 18)
    print(edad < 18)

## 4. Operadores lógicos

Permiten combinar condiciones.

- and: ambas condiciones deben ser verdaderas.
- or: al menos una condición debe ser verdadera.
- not: invierte el resultado de una condición.

Ejemplo:

    edad = 20
    tiene_permiso = True

    print(edad >= 18 and tiene_permiso)
    print(edad < 18 or tiene_permiso)
    print(not tiene_permiso)

## 5. ¿Qué es una expresión?

Una expresión es una combinación de valores, variables y operadores que produce un resultado.

Ejemplo:

    resultado = 10 + 5 * 2
    print(resultado)

## Resumen

Los operadores permiten realizar cálculos, comparar valores y combinar condiciones.

Son fundamentales para construir programas que puedan tomar decisiones y procesar información.
