# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: THANH PHUNG
# Section: 570
# Assignment: Lab Topic 5
# Date: 21 AUGUST 2026

from math import *

temp = float(input('Enter the excess temperature: '))

# check if temperature is in the range (1.3 and above)
if temp >= 1.3 and temp <= 1200:
    # each stage represent different intervals the temp in
    # each stage contain different slop formula
    if (temp >= 1.3 and temp <= 5):
        # m is the slope 
        m = (log10(7000/1000))/(log10(5/1.3))

        flux = 1000 * pow((temp / 1.3), m)

    elif (temp > 5 and temp <= 30):
        # m is the slope 
        m = (log10(1.5E6/7000))/(log10(30/5))

        flux = 7000 * pow((temp / 5), m)

    elif (temp > 30 and temp <= 120):
        m = (log10(2.5E4/1.5E6))/(log10(120/30))

        flux = 1.5E6 * pow((temp / 30), m)

    elif (temp > 120 and temp <= 1200):
        m = (log10(1.5E6/2.5E4))/(log10(1200/120))

        flux = 2.5E4 * pow((temp / 120), m)
    print(f'The surface heat flux is approximately {flux:.0f} W/m^2')

# if not, say the flux isn't avaliable
# this can be look at as special or edge case
elif temp < 1.3 or temp > 1200:
    flux = 'Surface heat flux is not available'
    print(flux)

