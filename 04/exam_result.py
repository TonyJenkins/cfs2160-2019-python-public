#!/usr/bin/env python3

"""
    Process five student marks to find the average.

    Display average along with the student's name.
"""

__author__  = "Tony Jenkins"
__email__   = "tony.jenkins@elder-studios.co.uk"
__date__    = "2018-09-30"
__license__ = "Unlicense"

NUMBER_OF_MARKS = 2

name = input ('Enter the student\'s name: ')

marks = []

for m in range (NUMBER_OF_MARKS):

    while 1:

        mark = int (input ('Enter result #' + str (m) + ':  '))

        if mark < 0 or mark > 100:
            print ('Out of range. Try again, dumbo.')
        else:
            marks.append (mark)
            break

total_marks = sum (marks)

average_mark = total_marks / NUMBER_OF_MARKS

print ()
print ('Final Mark for ' + name + ' is ' + str (average_mark) + '.')

if average_mark >= 50:
    print (f'Congrats, {name} has passed.')
