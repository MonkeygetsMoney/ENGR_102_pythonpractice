# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: THANH PHUNG
# Section: 570
# Assignment: Lab Topic 4
# Date: 11 SEPTEMBER 2026

# input day
day = float(input('Please enter a positive value for day: '))

# detect bigger than 0
if (day > 0 and day != ValueError):
    if(day <= 10):
        count = 10
        produce = day * count
    elif(day > 10 and day <= 50):
        count = day - 11 + 1
        produce = count * (day+11) * 1/2 + 100
    elif(day > 50 and day <= 100):
        count = 50 * (day-50)
        produce = 40 * (50+11) * 1/2 + 100 + count
    elif (day > 100):
        produce = 3820
    print(f'The sum total number of gadgets produced on day {day:.0f} is {produce:.0f}')

else:
    print('You entered an invalid number!')
    
