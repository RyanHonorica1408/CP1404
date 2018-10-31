"""
CP1404 Practical 10 - Ryan Honorica
Testing Code
"""

import doctest
from car import Car


def run_tests():
    def repeat_string(s, n):
        return " ".join([s] * n)

    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"
    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"
    test_car = Car(fuel=10)
    assert test_car.fuel == 10
    test_car = Car()
    assert test_car.fuel == 0


def phrase_to_sentence(term):
    """
    Format a phrase as a sentence, starting with a capital and ending with a .
    >>> phrase_to_sentence('hello')
    'Hello.'
    >>> phrase_to_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> phrase_to_sentence('Your next line will be.')
    'Your next line will be.'
    """
    new_term = term.capitalize()
    if new_term[-1] != '.':
        new_term += '.'
    return new_term



def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length

run_tests()

doctest.testmod()
