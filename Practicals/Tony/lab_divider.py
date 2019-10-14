"""
  Divide students into lab groups.
"""

__author__  = "Tony Jenkins"
__email__   = "tony.jenkins@elder-studios.co.uk"
__licence__ = "The Unlicense"
__version__ = "2019-10-10"

NUMBER_OF_PCS_IN_LAB = 24

try:
    number_of_students = int (input ('Enter the number of students: '))

    if number_of_students < 0:
        print ('Please enter a positive number of students.')
    else:
        number_of_labs = number_of_students // NUMBER_OF_PCS_IN_LAB

        if number_of_students % NUMBER_OF_PCS_IN_LAB != 0:
            number_of_labs += 1

        if number_of_labs == 1:
            print ('You need', number_of_labs, 'lab for the students.')
        else:
            print ('You need', number_of_labs, 'labs for the students.')

except ValueError:
    print ('Please enter an integer.')
