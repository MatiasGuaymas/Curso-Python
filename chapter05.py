# Exercise 5.14.1
'''
Ask a virtual assistant, “What are some uses of the modulus operator?”

Python provides operators to compute the logical operations and, or, and not, but it doesn’t have an operator that computes the exclusive or operation, usually written xor. Ask an assistant “What is the logical xor operation and how do I compute it in Python?”

In this chapter, we saw two ways to write an if statement with three branches, using a chained conditional or a nested conditional. You can use a virtual assistant to convert from one to the other. For example, ask a VA, “Convert this statement to a chained conditional.”

if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')

Ask a VA, “Rewrite this statement with a single conditional.”

if 0 < x:
    if x < 10:
        print('x is a positive single-digit number.')

See if a VA can simplify this unnecessary complexity.

if not x <= 0 and not x >= 10:
    print('x is a positive single-digit number.')

Here’s an attempt at a recursive function that counts down by two.

def countdown_by_two(n):
    if n == 0:
        print('Blastoff!')
    else:
        print(n)
        countdown_by_two(n-2)
But it has an error. Ask a virtual assistant what’s wrong and how to fix it. Paste the solution it provides back here and test it.
'''

'''
1. ¿Cuáles son algunos usos del operador módulo (%)?
Encontrar si un número es par o impar (n % 2 == 0)
Obtener el último dígito de un número (n % 10)
Trabajar con ciclos o repeticiones (por ejemplo, cada 7 días: dia % 7)
Comprobar divisibilidad (n % d == 0)
Calcular el “wrap around” en listas o secuencias circulares

2. ¿Qué es la operación lógica xor y cómo se hace en Python?
El xor lógico (o “o exclusivo”) es verdadero si exactamente uno de los operandos es verdadero, pero no ambos.
En Python, para valores booleanos: a != b o usando el operador ^ (a partir de Python 3.0): a ^ b
'''
x = 5
y = 7

# 3.
if x == y:
    print('x and y are equal')
elif x < y:
    print('x is less than y')
else:
    print('x is greater than y')

# 4.
if 0 < x < 10:
    print('x is a positive single-digit number.')

# 5.
if 0 < x < 10:
    print('x is a positive single-digit number.')

# 6: El error es que si n es negativo, la recursión nunca termina. Debe detenerse tanto en 0 como en valores negativos. Solución:
def countdown_by_two(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown_by_two(n-2)
countdown_by_two(5)

# Exercise 5.14.2
'''
The time module provides a function, also called time, that returns returns the number of seconds since the “Unix epoch”, which is January 1, 1970, 00:00:00 UTC (Coordinated Universal Time).
Use integer division and the modulus operator to compute the number of days since January 1, 1970 and the current time of day in hours, minutes, and seconds.
'''
import time
current_time = int(time.time())
days_since_epoch = current_time // (24 * 3600)
remaining_seconds = current_time % (24 * 3600)
hours = remaining_seconds // 3600
minutes = (remaining_seconds % 3600) // 60
seconds = remaining_seconds % 60
print(f"Days since epoch: {days_since_epoch}, Time of day: {hours}h {minutes}m {seconds}s")

# Exercise 5.14.3
'''
Write a function named is_triangle that takes three integers as arguments, and that prints either “Yes” or “No”, depending on whether you can or cannot form a triangle from sticks with the given lengths. Hint: Use a chained conditional.
'''
def is_triangle(a, b, c):
    """Determina si tres longitudes pueden formar un triángulo."""
    if a + b > c and a + c > b and b + c > a:
        print("Yes")
    else:
        print("No")
is_triangle(3, 4, 5)  # Yes
is_triangle(1, 2, 3)  # No

# Exercise 5.14.4
'''
What is the output of the following program? Draw a stack diagram that shows the state of the program when it prints the result.
'''
def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

recurse(3, 0)
'''
Diagrama de pila:
recurse(3, 0)
recurse(2, 3)
recurse(1, 5)
recurse(0, 6)
Output: 6
'''