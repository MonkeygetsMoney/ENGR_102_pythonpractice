# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: THANH PHung
# Section: 570
# Assignment: Lab Topic 1
# Date: 28 AUGUST 2026


from math import*

#This is a comment
#use it to tell what this code is doing

#calculate the area of rectangle
#length of 5 and height of 3

#print('Area of rectangle is', 5*3, 'in^2')
#the line can be spaced by comma


#Reynolds Number - fluid mechanics equation
##predict flowpatterns in different fluid flow situations

#Re = uL/v
##u - fluid with velocity
##v - kinematic viscosity
##L - characteristic linear dimension
print('Reynolds number is', (9*0.875)/0.0015)


#Bragg's Law - the scattering of waves from a crystal
#n*lambda = 2dsin(theta)
##n - order of diffraction (whole number)
##lambda - wavelength of the incident x-ray beam (our goal)
##distance/spacing bwteen atomic layers
##angle - angle between the incident beam and crystal plane
print('Wavelength is', (2*0.030*sin(radians(35))), 'nm')


#Arps equation - forecast future production rates of oil and gaswells
#q(t) = q(i)/(1 + bD(i)t)^(1/b)  (production rates)
#q(i) - initial production rate
#D(i) - initial decline rate
#b - hyperbolic constant
denom = 1 + 0.8*2*10
print('Production rate is',  100/pow(1 + 0.8*2*10, 1/0.8), 'barrels/day')


#Tsiolkovsky rocket equation - device can can create its own
#acceleration by removing its own mass with high velocity
#deltaV = ExhaustV * ln(Mi / Mf)
print('Change of velocity is', 2030*log(11000/8300), 'm/s')
