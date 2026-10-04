# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Jade Kim
#               Sohan Manjunath
#               Thanh Phung
#               Quang La
# Section:      570
# Assignment:   Lab 2
# Date:         29 SEPTEMBER 2026

from math import*

# get input from user
length = float(input('Enter the side length in meters: '))
layer = float(input('Enter the number of layers: '))

# cummulative sum of number of layer to 1
sum = layer*(layer + 1) / 2

# area needed for the sides
side = sum * 4 * pow(length,2)

# area needed from the top view
topside = pow(layer, 2) * pow(length,2)

area = side + topside

print(f'You need {area:.2f} m^2 of gold foil to cover the pyramid')