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
    for counter in range(6):
        reading = float(input("Please enter temp: " + str(counter + 1)))
        temp_list.append(reading)

    #print(temp_list)
    print("Max temp is:", max(temp_list))
    print("Min temp is:", min(temp_list))
    avg = sum(temp_list) / len(temp_list)
    rounded = round(avg, 2)
    print("Avg temp is", rounded)
except ValueError:
    print("Numbers only please)")

