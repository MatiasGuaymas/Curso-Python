# Exercise 8.12.1
'''
In this chapter, we only scratched the surface of what regular expressions can do. To get an idea of what’s possible, ask a virtual assistant, “What are the most common special characters used in Python regular expressions?”

You can also ask for a pattern that matches particular kinds of strings. For example, try asking:

Write a Python regular expression that matches a 10-digit phone number with hyphens.

Write a Python regular expression that matches a street address with a number and a street name, followed by ST or AVE.

Write a Python regular expression that matches a full name with any common title like Mr or Mrs followed by any number of names beginning with capital letters, possibly with hyphens between some names.

And if you want to see something more complicated, try asking for a regular expression that matches any legal URL.

A regular expression often has the letter r before the quotation mark, which indicates that it is a “raw string”. For more information, ask a virtual assistant, “What is a raw string in Python?”
'''

'''
Caracteres especiales más comunes en expresiones regulares de Python:

. (punto): cualquier carácter excepto salto de línea.
^: inicio de línea.
$: fin de línea.
*: cero o más repeticiones.
+: una o más repeticiones.
?: cero o una repetición (o modificador no codicioso).
{n,m}: entre n y m repeticiones.
[]: conjunto de caracteres.
|: alternancia (o).
\: escape de caracteres especiales.
() : agrupación y captura.

Expresión regular para un número de teléfono de 10 dígitos con guiones:
r"\d{3}-\d{3}-\d{4}"
Ejemplo válido: 123-456-7890

Expresión regular para una dirección con número, nombre de calle y ST o AVE:
r"\d+\s+[A-Za-z\s]+(?:ST|AVE)"
Ejemplo válido: 123 Main Street ST o 456 Elm AVE

Expresión regular para un nombre completo con título (Mr, Mrs) y nombres con mayúsculas, posibles guiones:
r"(Mr|Mrs)\.?\s([A-Z][a-z]+(-[A-Z][a-z]+)?\s?)+"
Ejemplo válido: Mr. John Smith o Mrs Mary-Jane Doe

Expresión regular para una URL legal:
r"https?://(?:www\.)?[\w\-]+(\.[\w\-]+)+[/\w\-\.\?\=\&\%]*"
Ejemplo válido: https://www.ejemplo.com/path?query=1

¿Qué es un “raw string” en Python? 
Un “raw string” (cadena cruda) se indica anteponiendo una r antes de las comillas, por ejemplo: r"\n". Esto hace que las secuencias de escape como \n o \t se interpreten literalmente y no como caracteres especiales, lo cual es muy útil en expresiones regulares.
'''

# Exercise 8.12.2
'''
See if you can write a function that does the same thing as the shell command !head. It should take as arguments the name of a file to read, the number of lines to read, and the name of the file to write the lines into. If the third parameter is None, it should display the lines rather than write them to a file.

Consider asking a virtual assistant for help, but if you do, tell it not to use a with statement or a try statement.
'''
def head(input_filename, n, output_filename=None):
    f = open(input_filename, 'r')
    lines = []
    for i in range(n):
        line = f.readline()
        if not line:
            break
        lines.append(line)
    f.close()
    if output_filename is None:
        for line in lines:
            print(line, end='')
    else:
        out = open(output_filename, 'w')
        for line in lines:
            out.write(line)
        out.close()

# head('ThinkPython\ejemplo.txt', 5)
# head('datos.txt', 10, 'salida.txt')

# Exercise 8.12.3
'''
“Wordle” is an online word game where the objective is to guess a five-letter word in six or fewer attempts. Each attempt has to be recognized as a word, not including proper nouns. After each attempt, you get information about which of the letters you guessed appear in the target word, and which ones are in the correct position.

For example, suppose the target word is MOWER and you guess TRIED. You would learn that E is in the word and in the correct position, R is in the word but not in the correct position, and T, I, and D are not in the word.

As a different example, suppose you have guessed the words SPADE and CLERK, and you’ve learned that E is in the word, but not in either of those positions, and none of the other letters appear in the word. Of the words in the word list, how many could be the target word? Write a function called check_word that takes a five-letter word and checks whether it could be the target word, given these guesses.

You can use any of the functions from the previous chapter, like uses_any.
'''
import re

def check_word(word):
    # Palabra debe ser de 5 letras exactamente
    if len(word) != 5:
        return False

    # Letras prohibidas (no están en la palabra)
    forbidden_letters = "SPADCLRK"

    # Si contiene alguna letra prohibida, no sirve
    if re.search(f"[{forbidden_letters}]", word):
        return False

    # La letra E debe estar en la palabra
    if 'E' not in word:
        return False

    # La letra E no puede estar en la posición 4 ni 5
    if word[3] == 'E' or word[4] == 'E':
        return False

    return True

print(check_word("THREE"))  # False (tiene R)
print(check_word("STEEP"))  # False (tiene S y P)
print(check_word("EVENT"))  # True

# Exercise 8.12.4
'''Continuing the previous exercise, suppose you guess the work TOTEM and learn that the E is still not in the right place, but the M is. How many words are left?
'''

# Exercise 8.12.5
'''
The Count of Monte Cristo is a novel by Alexandre Dumas that is considered a classic. Nevertheless, in the introduction of an English translation of the book, the writer Umberto Eco confesses that he found the book to be “one of the most badly written novels of all time”.

In particular, he says it is “shameless in its repetition of the same adjective,” and mentions in particular the number of times “its characters either shudder or turn pale.”

To see whether his objection is valid, let’s count the number number of lines that contain the word pale in any form, including pale, pales, paled, and paleness, as well as the related word pallor. Use a single regular expression that matches any of these words. As an additional challenge, make sure that it doesn’t match any other words, like impale – you might want to ask a virtual assistant for help.
'''
import re

# Expresión regular para pale, pales, paled, paleness y pallor (pero no impale)
pattern = re.compile(r"\b(pale(s|d|ness)?|pallor)\b", re.IGNORECASE)

count = 0

file = open('montecristo.txt', 'r', encoding='utf-8')

for line in file:
    if pattern.search(line):
        count += 1

print(f"Number of lines containing 'pale', 'pales', 'paled', 'paleness', or 'pallor': {count}")


