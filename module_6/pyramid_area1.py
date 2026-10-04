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

length = float(input('Enter the side length in meters: '))
layer = int(input('Enter the number of layers: '))
area = 0
area_one_face = 0
side = 0
topside = 0

for i in range (layer, 0, -1):
    area_one_face = pow(length,2)
    # this is the amount of face of the square

    side = i * 4 * area_one_face
    topside  = (pow(i, 2)* area_one_face - pow(i-1,2)* area_one_face)
    area += (side + topside)


print(f'You need {area:.2f} m^2 of gold foil to cover the pyramid')