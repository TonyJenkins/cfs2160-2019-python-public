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
__version__ = "2019-25-10"

temp_list = []
print("Welcome to the weather station")
try:
    counter = 0
    while counter < 6:
        reading = input("Please enter temp: " + str(counter + 1))

        if reading[-1].lower() in ("c", "f"):
            reading_cleaned = float(reading[:-1])

            if reading[-1].lower() == "f":
                reading_cleaned = (reading_cleaned - 32) / 1.8

            temp_list.append(reading_cleaned)
            counter += 1
        else:
            print("Please enter temps with c or f only")

    max = max(temp_list)
    min = min(temp_list)
    avg = sum(temp_list) / len(temp_list)
    rounded = round(avg, 2)

    print("Max temp is:", max, " F is:", (max * 1.8) + 32)
    print("Min temp is:", min)
    print("Avg temp is", rounded)
except ValueError:
    print("Numbers only please)")

