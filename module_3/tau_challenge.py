# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: THANH PHUNG
# Section: 570
# Assignment: Lab Topic 3
# Date: 06 SEPTEMBER 2026

from math import *

def decimals(num):
    digit = str(num)
    print(f'The value of tau to {num} digits is: {tau:.{num}f}')

num = int(input('Please enter the number of digits of precision for tau: '))
decimals(num)