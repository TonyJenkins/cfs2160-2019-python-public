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
temp_list = []
print("Welcome to the weather station")

try:
    for temp in range(6):
        temp_list.append(float(input("Please enter temp" + str(temp + 1))))

    max = max(temp_list)
    min = min(temp_list)
    avg = sum(temp_list) / len(temp_list)
    print("max temp is", max)
    print("Min temp is", min)
    print("Avg temp is", round(avg, 2))
except ValueError:
    print("Numbers only")








