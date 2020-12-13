#!/usr/bin/env python3

# Variable assignment: Here we create a variable called spam_amount and assign it the 
# value of 0 using =, which is called the assignment operator.
spam_amount = 0

# Function calls: print is a Python function that displays the value passed to it on the 
# screen. We call functions by putting parentheses after their name, and putting the inputs
# (or arguments) to the function in those parentheses.
print(spam_amount)

# In Python, comments begin with the # symbol.

# Reassigning the value of an existing variable. Python evaluates the expression on the
# right-hand-side of the = (0 + 4 = 4), and then assigns that value to the variable on the
# left-hand-side.
spam_amount = spam_amount + 4

# The colon ( :) at the end of the if line indicates that a new "code block" is starting. 
# Subsequent lines which are indented are part of that code block.
if spam_amount > 0:
    # Strings can be marked either by double or single quotation marks.
    print("But I don't want ANY spam!")

# The later lines dealing with viking_song are not indented with an extra 4 spaces, so
# they're not a part of the if 's code block.
# The * operator multiply a string by a number, to get a version that's been repeated that
# many times. (The technical term for this is operator overloading)
viking_song = "Spam " * spam_amount
print(viking_song)

# describe the type of thing that spam_amount is
type(spam_amount)

# float (a number with a decimal point)
type(19.95)

# arithmetic in python
5 + 2  # sum of 5 and 2
5 - 2  # difference of 5 and 2
5 * 2  # product of 5 and 2
5 / 2  # quotient of 5 and 2 (true division)
5 // 2 # quotient of 5 and 2, removing fractional parts (floor division)
5 % 2  # integer remainder after division of 5 by 2
5 ** 2 # 5 raised to the power of 2
-5     # the negative of 5 (negation)

# true division
print("true division of 5/2", 5/2)

# floor division
print("floor division of 5//2", 5//2)

# PEMDAS
hat_height_cm = 25
my_height_cm = 190
total_height_meters = (hat_height_cm + my_height_cm)/100
print("Height in meters =", total_height_meters)

# mininum and maximum of the arguments
print(min(1, 2, 3))
print(max(1, 2, 3))

# absolute value of the argument
print(abs(32))
print(abs(-32))

# type casting
print(float(10))
print(int(3.33))
print(int("807") + 1)
