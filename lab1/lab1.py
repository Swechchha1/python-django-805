"""
Jon Shallow
UNHM COMP705/805 Lab 1
An Introduction to Python
Jan 19, 2018

The purpose of this file is to learn BASIC python syntax and data structures.
There is an accompanying test file. Place both files in the same directory,
and then run:
$ python tests.py

You will see a print out of tests that are being run, and your result.
Please see: https://www.python.org/dev/peps/pep-0008/ for style guidelines
"""

def give_me_a_string():
    """
    This function returns a string value
    """
    fname = 'Swechchha '
    lname = 'Tiwari'
    return fname + lname

def give_me_an_integer():
    """
    This function returns an integer value
    """
    num1 = 5
    num2 = 2
    return num1 * num2

def give_me_a_boolean():
    """
    This function returns a boolean value
    """
    p = 10
    q = 10
    if p == q:
        result = True
    else:
        result = False
    return result


def give_me_a_float():
    """
    This function returns a float value
    """
    num1 = 25
    num2 = 4
    result = num1/num2
    return result



def give_me_a_list():
    """
    This function returns a list
    """
    desserts = ['oreo', 'pie', 'kitkat']
    if 'pie' in desserts:
        desserts.remove('pie')
    return desserts

def give_me_a_dictionary():
    """
    This function returns a dictionary
    """
    my_first_dictionary = {
                         "Android_upd" : 2017,
                         "Iphone_upd"  : 2018,
                         "mac_upd"     : 2017
                          }
    return my_first_dictionary

def give_me_a_tuple():
    """
    This function returns a tuple
    """
    temp_c = 30
    temp_f = temp_c * 9/5 + 32
    return temp_c, temp_f


def sum_numbers_one_to_ten():
    """
    This function returns the sum of all numbers one to ten
    Use the range function:
    https://docs.python.org/3/library/functions.html
    Use the accumulator pattern:
    http://interactivepython.org/runestone/static/thinkcspy/Functions/TheAccumulatorPattern.html
    """
    for m in range(1,11):
        total = 0
        for n in range(1,m+1):
            total = total + n
    return total



def check_is_even(number):
    """
    This function returns True if num is even
    else False
    hint: use modulo operator
    https://docs.python.org/3/reference/expressions.html
    """
    rem = number % 2
    if rem == 0:
        result = True
    else:
        result = False
    return result




def check_is_less_than(number1, number2):
    """
    This functions returns True if number1 < number2
    else False
    """
    if number1 < number2:
        result = True
    else:
        result = False
    return result



def factorial_of_num(number):
    """
    This function returns factorial of the number factorial_of_num
    test files
    """
    i = number - 1
    while i >= 1:
        number = number * i
        i = i - 1
    return number



def square_root(number):
    """ This fuction will return square root of a number """

    result = number**(1.0/2)
    return result
