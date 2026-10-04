# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: THANH PHUNG
# Section: 570
# Assignment: Lab Topic 3
# Date: 06 SEPTEMBER 2026

from math import*
print('This program calculates the Reynolds number given velocity, length, and viscosity')

#define all the variables here
v = float(input('Please enter the velocity (m/s): '))
L_dimension = float(input('Please enter the length (m): '))
u = float(input('Please enter the viscosity (m^2/s): '))
Re = (v*L_dimension)/u
print(f'Reynolds number is {Re:.0f}\n')

print('This program calculates the wavelength given distance and angle')
d = float(input('Please enter the distance (nm): '))
theta = float(input('Please enter the angle (degrees): '))
theta = radians(theta)
n = 1
wave = (2*d*sin(theta))/n
print(f'Wavelength is {wave:.4f} nm\n')

print('This program calculates the production rate given time, initial rate, and decline rate')
t = float(input('Please enter the time (days): '))
rate_in = float(input('Please enter the initial rate (barrels/day): '))
rate_de = float(input('Please enter the decline rate (1/day): '))
b = 0.8
denom = pow((1 + (b*rate_de*t)), 1/b)
q_t = rate_in/denom
print(f'Production rate is {q_t:.2f} barrels/day\n')

print('This program calculates the change of velocity given initial mass, final mass, and exhaust velocity')
mass_in = float(input('Please enter the initial mass (kg): '))
mass_fi = float(input('Please enter the final mass (kg): '))
v_ex = float(input('Please enter the exhaust velocity (m/s): '))
v_delta = v_ex*log(mass_in/mass_fi)
print(f'Change of velocity is {v_delta:.1f} m/s')