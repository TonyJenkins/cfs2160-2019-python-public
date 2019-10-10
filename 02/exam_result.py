#!/usr/bin/env python3

"""
    Process five student marks to find the average.

    Display average along with the student's name.
"""

__author__  = "Tony Jenkins"
__email__   = "tony.jenkins@elder-studios.co.uk"
__date__    = "2018-09-30"
__license__ = "Unlicense"

name = input ('Enter the student\'s name: ')

mark_1 = int (input ('Enter first result:  '))
mark_2 = int (input ('Enter second result: '))
mark_3 = int (input ('Enter third result:  '))
mark_4 = int (input ('Enter fourth result: '))
mark_5 = int (input ('Enter fifth result:  '))

total_marks = mark_1 + mark_2 + mark_3 + mark_4 + mark_5

average_mark = total_marks / 5

print ()
print ('Final Mark for ' + name + ' is ' + str (average_mark))
