#!/usr/bin/env python3

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

    print("Please enter the number of students in a class")

    number_of_students = int(input())

    number_of_room = number_of_students // 24
    remainder = number_of_students % 24

    if remainder > 0:
        number_of_room += 1
    if number_of_room != 1:
        print("You will need", number_of_room, "rooms")
    else:
        print("You will need", number_of_room, "room")
except ValueError:
    print("Please enter whole numbers only")

