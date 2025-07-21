# Exercise 2.11.1
'''
¿Por qué es malo usar int, float y str como nombres de variables?
Porque int, float y str son nombres de tipos incorporados en Python. Si usas estos nombres como variables, sobrescribes las referencias a los tipos originales, lo que puede causar errores y comportamientos inesperados en tu código.

¿Cuáles son las funciones incorporadas (built-in) en Python?
Algunas funciones incorporadas son: print(), len(), type(), int(), float(), str(), input(), abs(), sum(), min(), max(), round(), sorted(), range(), list(), dict(), set(), tuple(), help(), dir(), entre otras. 

¿Qué variables y funciones hay en el módulo math?
El módulo math incluye funciones como sqrt(), sin(), cos(), tan(), log(), exp(), pow(), factorial(), y constantes como pi y e. 

Además de math, ¿qué módulos se consideran parte del núcleo de Python?
Algunos módulos del núcleo de Python son: sys, os, random, datetime, time, re, json, collections, itertools, functools, statistics, pathlib, shutil, subprocess, y muchos más. Estos vienen incluidos con la instalación estándar de Python (la biblioteca estándar).
'''

# Excercise 2.11.2
'''
We’ve seen that n = 17 is legal. What about 17 = n?

How about x = y = 1?

In some languages every statement ends with a semi-colon (;). What happens if you put a semi-colon at the end of a Python statement?

What if you put a period at the end of a statement?

What happens if you spell the name of a module wrong and try to import maath?
'''
n = 17  # Esto es legal, asigna 17 a n
# 17 = n  # Esto no es legal, genera un error de sintaxis porque no se puede asignar un valor a una constante.
x = y = 1  # Esto es legal, asigna 1 tanto a x como a y
print("Hello, World!");  # Si pones un punto y coma al final, no pasa nada, Python lo ignora.
# Si pones un punto al final, generará un error de sintaxis porque Python espera una expresión válida.
# Si intentas importar un módulo con un nombre incorrecto, como maath, generará un error ImportError.

# Exercise: 2.11.3
'''
Part 1. The volume of a sphere with radius r is 4/3 * pi * r^3. What is the volume of a sphere with radius 5? Start with a variable named radius and then assign the result to a variable named volume. Display the result. Add comments to indicate that radius is in centimeters and volume in cubic centimeters.
'''
import math  
radius = 5 # El radio de la esfera en centímetros
volume = (4/3) * math.pi * (radius ** 3)  # El volumen de la esfera en centímetros cúbicos
print(volume)

'''
Part 2. A rule of trigonometry says that for any value of x, (cos x)^2 + (sin x)^2 = 1. Let’s see if it’s true for a specific value of x like 42.

Create a variable named x with this value. Then use math.cos and math.sin to compute the sine and cosine of x, and the sum of their squared.

The result should be close to 1. It might not be exactly 1 because floating-point arithmetic is not exact—it is only approximately correct.
'''
x = 42
cos_x = math.cos(x)
sin_x = math.sin(x)
print(cos_x ** 2 + sin_x ** 2) 

'''
Part 3. In addition to pi, the other variable defined in the math module is e, which represents the base of the natural logarithm, written in math notation as e. If you are not familiar with this value, ask a virtual assistant “What is math.e?” Now let’s compute three ways:
Use math.e and the exponentiation operator (**).
Use math.pow to raise math.e to the power 2.
Use math.exp, which takes as an argument a value x, and computes e^x.
'''
print(math.e ** 2)
print(math.pow(math.e, 2))
print(math.exp(2)) # Calcula e² usando una implementación interna más precisa y eficiente, sin depender del valor almacenado de math.e.