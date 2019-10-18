"""
    Calculate interesting weather statistics.
"""

__author__  = "Tony Jenkins"
__email__   = "tony.jenkins@elder-studios.co.uk"
__licence__ = "The Unlicense"
__version__ = "2019-10-17"

NUMBER_OF_READINGS = 6

castle_hill = []

for reading in range (NUMBER_OF_READINGS):
    while 1:
        try:
            temp = float (input ('Enter reading: '))
            castle_hill.append (temp)
            break
        except ValueError:
            print ('Please enter a number.')

average_temp = sum (castle_hill) / NUMBER_OF_READINGS
max_temp = max (castle_hill)
min_temp = min (castle_hill)

print ('Average Temp: ' + str (average_temp))
print ('Maximum Temp: ' + str (max_temp))
print ('Minimum Temp: ' + str (min_temp))
