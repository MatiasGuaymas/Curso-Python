# Exercise 4.11.1
'''
Write a function called rectangle that draws a rectangle with given side lengths.
'''
import turtle
def rectangle(width, height):
    for _ in range(2):
        turtle.forward(width) 
        turtle.left(90)       
        turtle.forward(height)
        turtle.left(90)       
turtle.speed(1)  
rectangle(80, 40) 

# Exercise 4.11.2
'''
Write a function called rhombus that draws a rhombus with a given side length and a given interior angle.
'''
def rhombus(side_length, angle):
    for _ in range(2):
        turtle.forward(side_length) 
        turtle.left(angle)          
        turtle.forward(side_length)
        turtle.left(180 - angle)
turtle.speed(1)
rhombus(80, 60)

# Exercise 4.11.3
'''
Now write a more general function called parallelogram that draws a quadrilateral with parallel sides. Then rewrite rectangle and rhombus to use parallelogram.
'''
def parallelogram(base, side, angle):
    turtle.forward(base) 
    turtle.left(angle)       
    turtle.forward(side)
    turtle.left(180 - angle)  
    turtle.forward(base) 
    turtle.left(angle)       
    turtle.forward(side)
    turtle.left(180 - angle)
turtle.speed(1)
def rectangle(width, height):
    parallelogram(width, height, 90)
def rhombus(side_length, angle):
    parallelogram(side_length, side_length, angle)
turtle.speed(1)
rectangle(80, 40)
rhombus(80, 60)

# Exercise 4.11.5
'''
4.11.5. Exercise
Write an appropriately general set of functions that can draw flowers like this.

Hint: Use arc to write a function called petal that draws one flower petal.
'''
import math

def arc(t, r, angle):
    """Dibuja un arco de radio r y ángulo en grados."""
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = angle / n

    for _ in range(n):
        t.forward(step_length)
        t.left(step_angle)

def petal(t, r, angle):
    """Dibuja un pétalo usando dos arcos"""
    for _ in range(2):
        arc(t, r, angle)
        t.left(180 - angle)

def flower(t, n, r, angle):
    """Dibuja una flor con n pétalos"""
    for _ in range(n):
        petal(t, r, angle)
        t.left(360 / n)

bob = turtle.Turtle()
bob.speed(0)
flower(bob, 7, 60, 60)  # n_pétalos, radio, ángulo
turtle.done()

# Exercise 4.11.6
'''
The following program uses a turtle graphics module to draw a circle:

from jupyturtle import make_turtle, forward, left
import math

def polygon(n, length):
    angle = 360 / n
    for i in range(n):
        forward(length)
        left(angle)
        
def circle(radius):
    circumference = 2 * math.pi * radius
    n = 30
    length = circumference / n
    polygon(n, length)
    
make_turtle(delay=0)
circle(30)

Write a function that draws a spiral.
'''
def spiral(turn_angle=20, step=2, growth=1, steps=100):
    """
    Dibuja una espiral con turtle.

    - turn_angle: el ángulo de giro en cada paso (grados)
    - step: longitud inicial del paso
    - growth: cuánto crece el paso en cada iteración
    - steps: cuántos pasos dar (cuánto se extiende la espiral)
    """
    for _ in range(steps):
        forward(step)
        left(turn_angle)
        step += growth  # hace que la espiral crezca

# Usar la función
make_turtle(delay=0)
spiral(turn_angle=20, step=2, growth=0.5, steps=150)