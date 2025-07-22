# Exercise 6.12.1
'''
In this chapter, we saw an incorrect function that can end without returning a value.

def absolute_value_wrong(x):
    if x < 0:
        return -x
    if x > 0:
        return x
And a version of the same function that has dead code at the end.

def absolute_value_extra_return(x):
    if x < 0:
        return -x
    else:
        return x
    
    return 'This is dead code.'
And we saw the following example, which is correct but not idiomatic.

def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False
Ask a virtual assistant what’s wrong with each of these functions and see if it can spot the errors or improve the style.

Then ask “Write a function that takes coordinates of two points and computes the distance between them.” See if the result resembles the version of distance we wrote in this chapter.
'''

'''
1. Problema: Si x es 0, la función no retorna nada (devuelve None). Falta un caso para x == 0.
2. Problema: La línea return 'This is dead code.' nunca se ejecuta, es código muerto (dead code) porque siempre se retorna antes.
3. Es correcto, pero no idiomático. Se puede simplificar así: 
def is_divisible(x, y):
    return x % y == 0
'''
import math
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Exercise 6.12.2
'''
Use incremental development to write a function called hypot that returns the length of the hypotenuse of a right triangle given the lengths of the other two legs as arguments.

Note: There’s a function in the math module called hypot that does the same thing, but you should not use it for this exercise!

Even if you can write the function correctly on the first try, start with a function that always returns 0 and practice making small changes, testing as you go. When you are done, the function should only return a value – it should not display anything.
'''
def hypot(a, b):
    return math.sqrt(a**2 + b**2)

# Exercise 6.12.3
'''
Write a boolean function, is_between(x, y, z), that returns True if x < y < z or if z < y < x and False otherwise.
'''
def is_between(x, y, z):
    return x < y < z or z < y < x

# Exercise 6.12.4
'''
Write a function named ackermann that evaluates the Ackermann function. What happens if you call ackermann(5, 5)?
'''
def ackermann(m, n):
    if m == 0:
        return n + 1
    else:
        if n == 0:
            return ackermann(m-1, 1)
        else:
            return ackermann(m-1, ackermann(m, n-1))
# print(ackermann(5, 5)) # Llamar a ackermann(5, 5) en Python no es práctico y causará un error de recursión o hará que el programa se congele.

# Exercise 6.12.5
'''
The greatest common divisor (GCD) of a and b is the largest number that divides both of them with no remainder.
One way to find the GCD of two numbers is based on the observation that if r is the remainder when a is divided by b, then gcd(a, b) = gcd(b, r). As a base case, we can use gcd(a, 0) = a.
Write a function called gcd that takes parameters a and b and returns their greatest common divisor.
'''
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
print(gcd(12, 6))