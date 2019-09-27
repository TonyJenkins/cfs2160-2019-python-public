#!/usr/bin/env python3

"""
    Can you rent the car?

    Apply a simple test to see if the user is old enough to rent a car.
"""

__author__  = "Tony Jenkins"
__email__   = "tony.jenkins@elder-studios.co.uk"
__licence__ = "The Unlicense"
__version__ = "2019-09-27"

print ('Hello, who are you? ')
name = input ()

print ('What year were you born?')
year = int (input ())

age_this_year = 2019 - year

print ('Good to meet you, ' + name + '.')
print ('This year you will be ' + str (age_this_year) + ' years old.')

if age_this_year >= 21:
    print ('So you can rent the car.')
else:
    print ('Sorry, you are too young to rent.')
