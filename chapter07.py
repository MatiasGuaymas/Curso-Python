# Exercise 7.9.1
'''
In uses_any, you might have noticed that the first return statement is inside the loop and the second is outside.

def uses_any(word, letters):
    for letter in word.lower():
        if letter in letters.lower():
            return True
    return False
When people first write functions like this, it is a common error to put both return statements inside the loop, like this.

def uses_any_incorrect(word, letters):
    for letter in word.lower():
        if letter in letters.lower():
            return True
        else:
            return False     # INCORRECT!
Ask a virtual assistant what’s wrong with this version.
'''
# El error en esta versión es que la función retorna True o False en la primera iteración del bucle, sin revisar todas las letras de la palabra. Así, solo evalúa la primera letra y no el resto.

# Exercise 7.9.2
'''
Write a function named uses_none that takes a word and a string of forbidden letters, and returns True if the word does not use any of the forbidden letters.

Here’s an outline of the function that includes two doctests. Fill in the function so it passes these tests, and add at least one more doctest.

def uses_none(word, forbidden):
    """Checks whether a word avoid forbidden letters.
    
    >>> uses_none('banana', 'xyz')
    True
    >>> uses_none('apple', 'efg')
    False
    """
    return None
'''
from doctest import run_docstring_examples
def uses_none(word, forbidden):
    """Checks whether a word avoid forbidden letters.
    
    >>> uses_none('banana', 'xyz')
    True
    >>> uses_none('apple', 'efg')
    False
    >>> uses_none('python', 'aeiou')
    False
    """
    for letter in word.lower():
        if letter in forbidden.lower():
            return False
    return True

def run_doctests(func):
    run_docstring_examples(func, globals(), name=func.__name__)

run_doctests(uses_none)

# Exercise 7.9.3
'''
Write a function called uses_only that takes a word and a string of letters, and that returns True if the word contains only letters in the string.

Here’s an outline of the function that includes two doctests. Fill in the function so it passes these tests, and add at least one more doctest.

def uses_only(word, available):
    """Checks whether a word uses only the available letters.
    
    >>> uses_only('banana', 'ban')
    True
    >>> uses_only('apple', 'apl')
    False
    """
    return None
'''
def uses_only(word, available):
    """Checks whether a word uses only the available letters.
    
    >>> uses_only('banana', 'ban')
    True
    >>> uses_only('apple', 'apl')
    False
    >>> uses_only('cab', 'abc')
    True
    """
    for letter in word.lower():
        if letter not in available.lower():
            return False
    return True

run_doctests(uses_only)

# Exercise 7.9.4
'''
Write a function called uses_all that takes a word and a string of letters, and that returns True if the word contains all of the letters in the string at least once.

Here’s an outline of the function that includes two doctests. Fill in the function so it passes these tests, and add at least one more doctest.

def uses_all(word, required):
    """Checks whether a word uses all required letters.
    
    >>> uses_all('banana', 'ban')
    True
    >>> uses_all('apple', 'api')
    False
    """
    return None
'''

def uses_all(word, required):
    """Checks whether a word uses all required letters.
    
    >>> uses_all('banana', 'ban')
    True
    >>> uses_all('apple', 'api')
    False
    >>> uses_all('matias', 'mat')
    True
    """
    for letter in required.lower():
        if letter not in word.lower():
            return False
    return True

run_doctests(uses_all)

# Exercise 7.9.5
'''
7.9.5. Exercise
The New York Times publishes a daily puzzle called “Spelling Bee” that challenges readers to spell as many words as possible using only seven letters, where one of the letters is required. The words must have at least four letters.

For example, on the day I wrote this, the letters were ACDLORT, with R as the required letter. So “color” is an acceptable word, but “told” is not, because it does not use R, and “rat” is not because it has only three letters. Letters can be repeated, so “ratatat” is acceptable.

Write a function called check_word that checks whether a given word is acceptable. It should take as parameters the word to check, a string of seven available letters, and a string containing the single required letter. You can use the functions you wrote in previous exercises.

Here’s an outline of the function that includes doctests. Fill in the function and then check that all tests pass.

def check_word(word, available, required):
    """Check whether a word is acceptable.
    
    >>> check_word('color', 'ACDLORT', 'R')
    True
    >>> check_word('ratatat', 'ACDLORT', 'R')
    True
    >>> check_word('rat', 'ACDLORT', 'R')
    False
    >>> check_word('told', 'ACDLORT', 'R')
    False
    >>> check_word('bee', 'ACDLORT', 'R')
    False
    """
    return False
According to the “Spelling Bee” rules,

Four-letter words are worth 1 point each.

Longer words earn 1 point per letter.

Each puzzle includes at least one “pangram” which uses every letter. These are worth 7 extra points!

Write a function called score_word that takes a word and a string of available letters and returns its score. You can assume that the word is acceptable.

Again, here’s an outline of the function with doctests.

def word_score(word, available):
    """Compute the score for an acceptable word.
    
    >>> word_score('card', 'ACDLORT')
    1
    >>> word_score('color', 'ACDLORT')
    5
    >>> word_score('cartload', 'ACDLORT')
    15
    """
    return 0
'''
def check_word(word, available, required):
    """Check whether a word is acceptable.

    >>> check_word('color', 'ACDLORT', 'R')
    True
    >>> check_word('ratatat', 'ACDLORT', 'R')
    True
    >>> check_word('rat', 'ACDLORT', 'R')
    False
    >>> check_word('told', 'ACDLORT', 'R')
    False
    >>> check_word('bee', 'ACDLORT', 'R')
    False
    """
    word = word.lower()
    available = available.lower()
    required = required.lower()
    if len(word) < 4:
        return False
    if not uses_only(word, available):
        return False
    if required not in word:
        return False
    return True

def word_score(word, available):
    """Compute the score for an acceptable word.

    >>> word_score('card', 'ACDLORT')
    1
    >>> word_score('color', 'ACDLORT')
    5
    >>> word_score('cartload', 'ACDLORT')
    15
    """
    word = word.lower()
    available = available.lower()
    if len(word) == 4:
        return 1
    score = len(word)
    if uses_all(word, available):
        score += 7
    return score

run_doctests(check_word)
run_doctests(word_score)

# Exercise 7.9.6
'''
You might have noticed that the functions you wrote in the previous exercises had a lot in common. In fact, they are so similar you can often use one function to write another.

For example, if a word uses none of a set forbidden letters, that means it doesn’t use any. So we can write a version of uses_none like this.

def uses_none(word, forbidden):
    """Checks whether a word avoids forbidden letters.
    
    >>> uses_none('banana', 'xyz')
    True
    >>> uses_none('apple', 'efg')
    False
    >>> uses_none('', 'abc')
    True
    """
    return not uses_any(word, forbidden)
There is also a similarity between uses_only and uses_all that you can take advantage of. If you have a working version of uses_only, see if you can write a version of uses_all that calls uses_only.
'''
def uses_all(word, required):
    """Checks whether a word uses all required letters."""
    return uses_only(required, word)

# Exercise 7.9.7
'''
7.9.7. Exercise
If you got stuck on the previous question, try asking a virtual assistant, “Given a function, uses_only, which takes two strings and checks that the first uses only the letters in the second, use it to write uses_all, which takes two strings and checks whether the first uses all the letters in the second, allowing repeats.”

Use run_doctests to check the answer.
'''
run_doctests(uses_all)

# Exercise 7.9.8
'''
Now let’s see if we can write uses_all based on uses_any.

Ask a virtual assistant, “Given a function, uses_any, which takes two strings and checks whether the first uses any of the letters in the second, can you use it to write uses_all, which takes two strings and checks whether the first uses all the letters in the second, allowing repeats.”

If it says it can, be sure to test the result!

# Here's what I got from ChatGPT 4o December 26, 2024
# It's correct, but it makes multiple calls to uses_any 

def uses_all(s1, s2):
    """Checks if all characters in s2 are in s1, allowing repeats."""
    for char in s2:
        if not uses_any(s1, char):
            return False
    return True
'''

def uses_all(s1, s2):
    """Checks if all characters in s2 are in s1, allowing repeats."""
    for char in s2:
        if not uses_any(s1, char):
            return False
    return True

