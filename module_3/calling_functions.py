# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: THANH PHUNG
# Section: 570
# Assignment: Lab Topic 3
# Date: 06 SEPTEMBER 2026

from math import *

def printresult(shape, side, area):
    '''Print the result of the calculation'''
    print(f'A {shape} with side {side:.2f} has area {area:.3f}')

side = float(input('Please enter the side length: '))

#area of triangle (define its variable)
height = (side/2)*sqrt(3)
area = 1/2 * (side * height)
printresult('triangle', side, area)

#area of square (define its variable)
area = pow(side, 2)
printresult('square', side, area)

#area of pentagon (define its variable)
sum = 5 + 2*sqrt(5)
coeff = 1/4 * (sqrt(5*(sum)))
area = pow(side, 2) * coeff
printresult('pentagon', side, area)

#area of hexagon (define its variable)
coeff = 3/2 *sqrt(3)
area = coeff * pow(side, 2)
printresult('hexagon', side, area)

#area of dodecagon
coeff = 3 * (2 + sqrt(3))
area = coeff * pow(side, 2)
printresult('dodecagon', side, area)