# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: THANH PHUNG
# Section: 570
# Assignment: Lab Topic 4
# Date: 11 SEPTEMBER 2026

# this is a program finding root using the quadratic formula
from math import*

a = float(input('Please enter the coefficient A: '))
b = float(input('Please enter the coefficient B: '))
c = float(input('Please enter the coefficient C: '))

#have a major detect the number of a
if(a != 0):
    b_sq = pow(b, 2)
    determinant = b_sq - 4*a*c

    # within a, compare the determinant
    if(determinant >= 0):
        root = sqrt(determinant)
        x_1 = (-b + root) / (2 * a)
        x_2 = (-b - root) / (2 * a)

        if (x_1 > x_2):
            print(f'The roots are x = {x_1:.1f} and x = {x_2:.1f}')
        elif (x_1 == x_2):
            print(f'The root is x = {x_1:.1f}')
        else:
            print(f'The roots are x = {x_2:.1f} and x = {x_2:.1f}')

    if(determinant < 0):
        root = sqrt(abs(determinant))
        root = root / (2*a)
        b = (-b) / (2*a)

        print(f'The roots are x = {b:.1f} + {root:.1f}i and x = {b:.1f} - {root:.1f}i')

# if a = 0, the equation turn into linear equation and we can 
# find c from there
elif (a == 0 and b != 0):
    x_1 = -c/b
    print(f'The root is x = {x_1:.1f}')

elif (a==0 and b == 0):
    print('You entered an invalid combination of coefficients!')