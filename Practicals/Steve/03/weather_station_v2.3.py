#!/usr/bin/env python3

"""
    capture and calculate temperature.
    TODO
    1, Print welcome message
    2, ask for 6 temperatures and store the results
    3, process the input
    4, process the results; min, max, avg
    5, Print the results
"""

__author__ = "Steve McGuire"
__email__ = "s.mcguire@hud.ac.uk"
__licence__ = "The Unlicense"
__version__ = "2019-25-10"

temp_list = []
print("Welcome to the weather station")
counter = 0
while counter < 6:
    # get the user input as string
    temp = input("please enter temp" + str(counter + 1))
    # check if last character in c or f
    if temp[-1].lower() in ("c", "f"):
        # remove the character from the end
        temp_cleaned = int(temp[:-1])
        #  check is last character is f, this tell us the reading was entered in fahrenheit
        if temp[-1] == "f":
            # if reading in f then convert from f to c
            temp_cleaned = (temp_cleaned - 32) / 1.8
        # append processed reading to the list
        temp_list.append(temp_cleaned)
        counter += 1
    else:
        print("please ensure inputs have c or f")
max = max(temp_list)
min = min(temp_list)
print("Max value is C is", max, "F is", (max + 32) * 1.8)
print("Min value is C is", min, "F is", (min + 32) * 1.8)
avg = sum(temp_list) / len(temp_list)
rounded = round(avg, 2)
print("Avg temp is C is", rounded)
