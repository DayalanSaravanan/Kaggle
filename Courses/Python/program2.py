#!/usr/bin/env python3

# defining functions

# Functions start with a header introduced by the def keyword. The indented block of code
# following the : is run when the function is called. return is another keyword uniquely
# associated with functions. When Python encounters a return statement, it exits the
# function immediately, and passes the value on the right hand side to the calling context.

# The docstring is a triple-quoted string (which may span multiple lines) that comes
# immediately after the header of a function. When we call help() on a function, it
# shows the docstring.

def least_difference(a, b, c):
    """ Return the smallest difference between any two numbers 
        among a, b, c.

        >>> least_difference(1, 5, -5)
        4
     """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)

print(least_difference(13, 24, 35))

# help function
help(least_difference)

# default arguments
print(1, 2, 3)
print(1, 2, 3, sep=' ')
print(1, 2, 3, sep=' < ')

# Adding optional arguments with default values to the functions we define turns out to be
# pretty easy.

def greet(who="World!"):
    print("Hello,", who)

greet()
greet(who="Universe!")
greet("Kaggle!")

# Functions applied to Functions
def mult_by_five(x):
    return 5*x

def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)

def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))

print(
        call(mult_by_five, 1),
        squared_call(mult_by_five, 1),
        sep='\n', # '\n' is the newline character - it starts a new line
     )
      
# Functions that operate on other functions are called "Higher order functions"
# By default, max returns the largest of its arguments. But if we pass in a function using 
# optional key argument, it returns the argument x that maximizes key(x) (aka the 'argmax')

def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x%5

print(
        'Which number is biggest?',
        max(100, 51, 14),
        'Which number is the biggest modulo 5?',
        max(100, 51, 14, key=mod_5),
        sep='\n'
     )
