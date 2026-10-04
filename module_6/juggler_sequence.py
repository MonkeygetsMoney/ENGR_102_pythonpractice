# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: THANH PHUNG
# Section: 570
# Assignment: Lab Topic 6
# Date: 29 SEPTEMBER 2026

from math import*

num = int(input('Enter a positive integer: '))
print(f'The Juggler sequence starting at {num} is:')

# number of iteration
count = 0
# string to append to 
if num == 1:
    string = f'{str(num)}'
else:
    string = f'{str(num)}, '

    while (num != 1):
        if (num % 2) == 0:
            # int to remove the decimal
            num = int(sqrt(num))
            if num == 1:
                string += str(num)
            else:
                string += str(num) + ', '

        elif (num % 2) == 1:
            num = int(pow(num, 3/2))
            if num == 1:
                string += str(num)
            else:
                string += str(num) + ', '
        count += 1

print(string)
print(f'It took {count} iterations to reach 1')
        