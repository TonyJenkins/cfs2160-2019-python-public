#!/usr/bin/env python3

'''
    Print to screen the number of labs for a given number of students.
    asdasdasd
'''


__author__  = "Saad Khan"
__email__   = "saad.khan@hud.ac.uk"
__licence__ = "The Unlicensed"
__version__ = "1"



number_of_pupils = int (input ('Enter the number of pupils: '))
number_of_sweets = int (input ('Enter the number of sweets: '))
print ('Number of sweets per pupil: ', number_of_sweets // number_of_pupils)
print ('Number of sweets left over: ', number_of_sweets % number_of_pupils)


side_1 = float (input ('Enter the length of side 1: '))
side_2 = float (input ('Enter the length of side 2: '))
print ('The area is %.2f units.' % (side_1 * side_2))


from math import pi
radius = float (input ('Enter the radius of the circle: '))
print ('The area is %.2f units.' % ((22/7) * radius * radius))


from math import pi
radius = float (input ('Enter the radius of the circle: '))
print ('The area is %.2f units.' % (pi * radius * radius))


fahrenheit = float (input ('Enter the temp in Fahrenheit: '))
print ('In Celsius that is %.2fF.' % ((fahrenheit - 32) * 5 / 9 ))

celsius = float (input ('Enter the temp in Celsius: '))
print ('In Fahrenheit that is %.2fF.' % (celsius * 9/5 + 32))


name = input ('Hello, who are you? ')
print ('Hello, ' + name + '. It is good to meet you.')


marks = []
for counter in range (4):
    marks.append (float (input ('Mark #' + str (counter + 1) + ': ')))
print ('Maximum marks:', max (marks))
print ('Minimum marks:', min (marks))
print ('Average marks:', round (sum (marks) / len (marks), 2))


print ('Please enter the readings (non-numeric to terminate).')
readings = []
counter = 1
while True: 
	reading  = input('Enter reading #' + str (counter) + ': ')
	try:
		readings.append(int(reading))		
	except ValueError:
		break		
	counter = counter + 1
	
print ('Maximum reading:', max (readings))
print ('Minimum reading:', min (readings))
print ('Average reading:', round (sum (readings) / len (readings), 2))
