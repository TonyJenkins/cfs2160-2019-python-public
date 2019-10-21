"""
    Calculate interesting weather statistics.
"""

__author__  = "Tony Jenkins"
__email__   = "tony.jenkins@elder-studios.co.uk"
__licence__ = "The Unlicense"
__version__ = "2019-10-17"

NUMBER_OF_READINGS = 6

castle_hill = []

try:
    for reading in range (NUMBER_OF_READINGS):
        temp = float (input ('Enter reading: '))
        castle_hill.append (temp)

    print ('Maximum Temp:', max (castle_hill))
    print ('Minimum Temp:', min (castle_hill))
    print ('Average Temp:', sum (castle_hill) / NUMBER_OF_READINGS)
except ValueError:
    print ('Non-number found in input. Sorry.')
