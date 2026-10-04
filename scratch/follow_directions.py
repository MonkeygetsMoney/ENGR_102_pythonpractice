# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: THANH PHUNG
# Section: 570
# Assignment: Lab Topic 1
# Date: 28 AUGUST 2026

from math import*

print('This shows the evaluation of (1-cos(x))/x^2 evaluated close to x=0')
print('My guess is 1/2')
#decimal in x will be one place in each print line
#this show x get closer and closer to zero

print((1 - cos(1.0))/1.0)
print((1 - cos(0.1))/pow(0.1, 2))
print((1 - cos(0.01))/pow(0.01, 2))
print((1 - cos(0.001))/pow(0.001, 2))
print((1 - cos(0.0001))/pow(0.0001, 2))
print((1 - cos(0.00001))/pow(0.00001, 2))
print((1 - cos(0.000001))/pow(0.000001, 2))
print((1 - cos(0.0000001))/pow(0.0000001, 2))
print('')
print('My guess was way off!')

#print('Maybe next time, it will be a little bit better')