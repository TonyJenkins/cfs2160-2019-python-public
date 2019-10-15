#!/usr/bin/env python3
import math
"""
    TASK - Print to screen the number of labs for a given number of students.
    TODO (Primary path)
    1, print welcome message
    2, get number of students
    3, divide number of students by the number of pcs in a room (need discussion - many ways to do this!)
    4, print out the result with meaningful message.
"""

__author__  = "Steve McGuire"
__email__   = "s.mcguire@hud.ac.uk"
__licence__ = "The Unlicense"
__version__ = "2019-10-11"

try:
    print("Hello, please enter the number of students")
    number_of_students = int(input())
    number_of_rooms = math.ceil(number_of_students / 24)

    if number_of_rooms == 1:
        print("you will need ", number_of_rooms)
    else:
        print("you will need ", number_of_rooms, "s")

except ValueError:
    print("Please enter a number only")
