# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: THANH PHUNG
# Section: 570
# Assignment: Lab Topic 4
# Date: 11 SEPTEMBER 2026

num = float(input('Enter number 1: '))
num2 = float(input('Enter number 2: '))
num3 = float(input('Enter number 3: '))

# define x to print
x = 0

# compare to print
if num >= num2:
    x = num
    if x >= num3:
        x = num
    else:
        x = num3
else:
    x = num2
    if x >= num3:
        x = num2
    else:
        x = num3
x = str(x)

print(f'The largest number is {x}')