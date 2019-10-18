#!/usr/bin/env python3

"""
    capture and calculate temperature.
    TODO
    1, Print welcome message
    2, ask for 6 temperatures and store the results
    3, process the results; min, max, avg
    4, Print the results
"""

__author__ = "Steve McGuire"
__email__ = "s.mcguire@hud.ac.uk"
__licence__ = "The Unlicense"
__version__ = "2019-15-10"

print("Welcome to the weather station")

temp_list = []

try:
    for counter in range(6):
        temp_1 = float(input("Please enter temp: " + str(counter + 1)))
        temp_list.append(temp_1)
except ValueError:
    print("Please enter numbers only")

print("Max value is" + str(max(temp_list)))
print("Min value is" + str(min(temp_list)))

avg = sum(temp_list) / len(temp_list)
rounded = round(avg, 2)
print("Avg is" + str(rounded))
