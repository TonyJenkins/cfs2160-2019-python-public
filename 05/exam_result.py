#!/usr/bin/env python3

"""
    Process five student marks to find the average.

    Display average along with the student's name.
"""

__author__  = "Tony Jenkins"
__email__   = "tony.jenkins@elder-studios.co.uk"
__date__    = "2019-11-13"
__license__ = "Unlicense"

from math import ceil

NUMBER_OF_MARKS = 5
PASS_MARK = 50

def student_passed (student_mark):
    return student_mark >= PASS_MARK

def average (list_of_numbers):
    return sum (list_of_numbers) / len (list_of_numbers)

def valid_mark (mark):
    return mark in range (0, 101)

if __name__ == '__main__':

    name = input ('Enter the student\'s name: ')

    marks = []

    for m in range (1, NUMBER_OF_MARKS + 1):

        while 1:

            mark = int (input (f'Enter result #{m}: '))

            if not valid_mark (mark):
                print ('Out of range. Try again.')
            else:
                marks.append (mark)
                break

    average_mark = average (marks)

    print ()
    print (f'Final Mark for {name} is {ceil (average_mark)}%.')

    if student_passed (ceil (average_mark)):
        print (f'Congrats, {name} has passed.')
    else:
        print (f'Sadly, {name} has failed.')
