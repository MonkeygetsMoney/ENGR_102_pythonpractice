# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: THANH PHUNG
# Section: 570
# Assignment: Lab Topic 6
# Date: 29 SEPTEMBER 2026

num_1 = int(input('Enter an integer: '))
num_2 = int(input('Enter another integer: '))
number = 0

# append for every number
for i in range(num_1, num_2 + 1, 1):
    number += i

print(f'The sum of all integers from {num_1} to {num_2} is {number:.0f}')