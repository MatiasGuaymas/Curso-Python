# Exercise 3.11.1
'''
Ask your favorite VA to “Write a function called repeat that takes a string and an integer and prints the string the given number of times.”

If the result uses a for loop, you could ask, “Can you do it without a for loop?”

Pick any other function in this chapter and ask a VA to write it. The challenge is to describe the function precisely enough to get what you want. Use the vocabulary you have learned so far in this book.
'''
def repeat(string, times):
    """Imprime la cadena 'string' 'times' veces."""
    for _ in range(times):
        print(string)
repeat("Hola, Python!", 3)  # Imprime "Hola, Python!" tres veces
'''
Ask a VA what’s wrong with this version of print_twice.

def print_twice(string):
    print(cat)
    print(cat)
'''
# La variable 'cat' no está definida en la función. Debería ser 'string' en lugar de 'cat'.

# Excercise 3.11.2
'''
Write a function named print_right that takes a string named text as a parameter and prints the string with enough leading spaces that the last letter of the string is in the 40th column of the display.

Hint: Use the len function, the string concatenation operator (+) and the string repetition operator (*).

Here’s an example that shows how it should work.

print_right("Monty")
print_right("Python's")
print_right("Flying Circus")
                                   Monty
                                Python's
                           Flying Circus
'''
def print_right(text):
    spaces_needed = 40 - len(text)
    print(' ' * spaces_needed + text)
print_right("Hola, Python!")  

# Excercise 3.11.3
'''
Write a function called triangle that takes a string and an integer and draws a pyramid with the given height, made up using copies of the string. Here’s an example of a pyramid with 5 levels, using the string 'L'.

triangle('L', 5)
L
LL
LLL
LLLL
LLLLL
'''
def triangle(string, height):
    for i in range(1, height + 1):
        print(string * i)
triangle('L', 5) 

# Excercise 3.11.4
'''
3.11.4. Exercise
Write a function called rectangle that takes a string and two integers and draws a rectangle with the given width and height, made up using copies of the string. Here’s an example of a rectangle with width 5 and height 4, made up of the string 'H'.

rectangle('H', 5, 4)
HHHHH
HHHHH
HHHHH
HHHHH
'''
def rectangle(string, width, height):
    for i in range(height):
        print(string * width)
rectangle('H', 5, 4)

# Exercise 3.11.5
'''
The song “99 Bottles of Beer” starts with this verse:

99 bottles of beer on the wall
99 bottles of beer
Take one down, pass it around
98 bottles of beer on the wall

Then the second verse is the same, except that it starts with 98 bottles and ends with 97. The song continues – for a very long time – until there are 0 bottles of beer.

Write a function called bottle_verse that takes a number as a parameter and displays the verse that starts with the given number of bottles.

Hint: Consider starting with a function that can print the first, second, or last line of the verse, and then use it to write bottle_verse.

Use this function call to display the first verse.

bottle_verse(99)
99 bottles of beer on the wall
99 bottles of beer 
Take one down, pass it around
98 bottles of beer on the wall
If you want to print the whole song, you can use this for loop, which counts down from 99 to 1. You don’t have to completely understand this example—we’ll learn more about for loops and the range function later.

for n in range(99, 0, -1):
    bottle_verse(n)
    print()
'''
def bottle_verse(num):
    print(num, 'bottles of beer on the wall')
    print(num, 'bottles of beer')
    print('Take one down, pass it around')
    print(num-1, 'bottles of beer on the wall')

for n in range(99, 0, -1):
    bottle_verse(n)
    print()