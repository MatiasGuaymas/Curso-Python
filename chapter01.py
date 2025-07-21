# Exercise: 1.9.2
print(round(42.5))
print(round(43.5))

'''
If you are curious, ask a virtual assistant, "If a number ends in 0.5, does Python round up or down?"
En Python, la función round() utiliza el método de redondeo "al par más cercano" (también llamado "round half to even" o "banco"). Esto significa que si un número termina en .5, Python lo redondea al número par más cercano.
'''

# Exercise: 1.9.3
# You can use a minus sign to make a negative number like -2. What happens if you put a plus sign before a number? What about 2++2?
print(+2) # Imprime 2
print(2++2) # Imprime 4

''' 
What happens if you have two values with no operator between them, like 4 2?
Lo que pasa es que Python no puede interpretar esto como una expresión válida y generará un error de sintaxis.
'''

'''
If you call a function like round(42.5), what happens if you leave out one or both parentheses?
Si dejas fuera uno o ambos paréntesis, Python no ejecutará la función. En lugar de eso, te devolverá una referencia a la función misma o generará un error si se espera un argumento.
'''

# Exercise: 1.9.4
'''
What is the type of the value of the following expressions? Make your best guess for each one, and then use type to find out.

765

2.718

'2 pi'

abs(-7)

abs(-7.0)

abs

int

type
'''
print(type(765))        # <class 'int'>
print(type(2.718))      # <class 'float'>
print(type('2 pi'))     # <class 'str'>
print(type(abs(-7)))    # <class 'int'>
print(type(abs(-7.0)))  # <class 'float'>
print(type(abs))        # <class 'builtin_function_or_method'>
print(type(int))        # <class 'type'>
print(type(type))       # <class 'type'>

# Exercise: 1.9.5
'''
How many seconds are there in 42 minutes 42 seconds?

How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.

If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace in seconds per mile?

What is your average pace in minutes and seconds per mile?

What is your average speed in miles per hour?
'''
# 42 minutos y 42 segundos a segundos
seconds_in_42_minutes_42_seconds = 42 * 60 + 42
print(seconds_in_42_minutes_42_seconds)  # 2562 segundos

# 10 kilómetros a millas
miles_in_10_kilometers = 10 / 1.61
print(miles_in_10_kilometers)  # Aproximadamente 6.213 millas

# Promedio de ritmo en segundos por milla
average_pace_seconds_per_mile = seconds_in_42_minutes_42_seconds / miles_in_10_kilometers
print(average_pace_seconds_per_mile)  # Aproximadamente 412.5 segundos por milla

# Promedio de ritmo en minutos y segundos por milla
average_pace_minutes = average_pace_seconds_per_mile // 60
average_pace_seconds = average_pace_seconds_per_mile % 60
print(f"Average pace: {int(average_pace_minutes)} minutes and {int(average_pace_seconds)} seconds per mile")  # Aproximadamente 6 minutos y 52 segundos por milla

# Promedio de velocidad en millas por hora
average_speed_miles_per_hour = miles_in_10_kilometers / (seconds_in_42_minutes_42_seconds / 3600)
print(average_speed_miles_per_hour)  # Aproximadamente 13.9 millas por hora