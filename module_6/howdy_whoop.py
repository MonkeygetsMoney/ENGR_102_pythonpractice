# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: THANH PHUNG
# Section: 570
# Assignment: Lab Topic 6
# Date: 29 SEPTEMBER 2026

# this program takes 2 integers and check if they're
# divisible by numbers from 1 to 100

num_1 = int(input('Enter an integer: '))
num_2 = int(input('Enter another integer: '))

for i in range(100):
    number = i + 1
    if (number % num_1 == 0) and (number % num_2 == 0):
        print('Howdy Whoop')
    elif number % num_1 == 0:
        print('Howdy')
    elif number % num_2 == 0:
        print('Whoop')
    else:
        print(number)