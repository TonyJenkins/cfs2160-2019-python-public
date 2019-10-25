#!/usr/bin/env python3

"""
    capture and calculate temperature.
    TODO
    1, Print welcome message
    2, ask for 6 temperatures and store the results
    3, process input
    4, process the results; min, max, avg
    5, Print the results
"""

__author__ = "Steve McGuire"
__email__ = "s.mcguire@hud.ac.uk"
__licence__ = "The Unlicense"
__version__ = "2019-25-10"

print("Welcome to the weather station")

temp_list = []

try:
    for counter in range(3):
        # get the user input as string
        temp = input("Please enter temp: " + str(counter + 1))
        # check if last character in c or f
        if temp[-1].lower() in ("c", "f"):
            # remove the character from the end
            temp_cleaned = int(temp[:-1])
            #  check is last character is f, this tell us the reading was entered in fahrenheit
            if temp[-1].lower() == "f":
                # if reading in f then convert from f to c
                temp_cleaned = (temp_cleaned - 32) / 1.8
            # append processed reading to the list
            temp_list.append(temp_cleaned)
        else:
            print("Please enter c or f only")
except ValueError:
    print("Please enter numbers only")

print("Max value is C" + str(max(temp_list)) +
      "F: " + str( (max(temp_list) + 32) * 1.8))
print("Min value is C" + str(min(temp_list)))

avg = sum(temp_list) / len(temp_list)
rounded = round(avg, 2)
print("Avg is C" + str(rounded))
