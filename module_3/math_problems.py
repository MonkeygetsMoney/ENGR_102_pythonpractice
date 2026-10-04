# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: THANH PHUNG
# Section: 570
# Assignment: Lab Topic 3
# Date: 09 SEPTEMBER 2026

from math import*

height = float(input('Enter the height of the door: '))
width = float(input('Enter the width of the door: '))

r = width/(sqrt(2))
area_tri = 1/2 * pow(r, 2)
arc_area = 1/4 * pi * pow(r,2) - area_tri

#define the height for only rectangle part
arc_height = r - (r* cos(radians(45)))
height = height - arc_height
area_rec = height*width 
door = area_rec + arc_area

print(f'The area of the door is {door:.2f}')

height = float(input('Enter the height of the pyramid: '))
#find side of triangle
area_tri = 4.46/4
side = area_tri*4/sqrt(3)
side = height*sqrt(side)
area_tri = sqrt(3)/4 * pow(side, 2)

area_square = pow(side, 2)
pyramid = area_square + 4*area_tri
print(f'The surface area of the pyramid is {pyramid:.2f}')






