#!/usr/bin/env python3
"""
    capture and calculate temperature.
    TODO
    1, Print welcome message
    2, ask for 6 temperatures and store the results
    3, process C or F
    4, process the results; min, max, avg
    5, Print the results
"""

__author__ = "Steve McGuire"
__email__ = "s.mcguire@hud.ac.uk"
__licence__ = "The Unlicense"
__version__ = "2019-15-10"
temp_list = []
print("Welcome to the weather station")
count = 0
try:
    for temp in range(3):
        # get the user input as string
        reading = input("Please enter temp" + str(temp + 1))
        # remove the character from the end
        reading_cleaned = float(reading[:-1])
        # check if last character in c or f
        if reading[-1].lower() in ("c", "f"):
            #  check is last character is f, this tell us the reading was entered in fahrenheit
            if reading[-1].lower() == "f":
                # if reading in f then convert from f to c
                reading_cleaned = (reading_cleaned - 32) / 1.8
            # append processed reading to the list
            temp_list.append(reading_cleaned)
        else:
            print("Please enter temp with c or f")

    max = max(temp_list)
    min = min(temp_list)
    avg = sum(temp_list) / len(temp_list)
    print("max temp C is", round(max,2), "F is:", round((max + 32) * 1.8, 2))
    print("max temp C is", round(min,2), "F is:", round((min + 32) * 1.8, 2))
    print("Avg temp C is", round(avg, 2), "F is:",round((min + 32) * 1.8, 2))
except ValueError:
    print("Numbers only")