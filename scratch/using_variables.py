# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: THANH PHUNG
# Section: 570
# Assignment: Lab Topic 1
# Date: 28 AUGUST 2026

#this is an improvement from print_math
#with the use of variable

from math import*

#Reynolds Number(Re)
u = 9
v = 0.0015
L_dimension = 0.875
Re = (u*L_dimension)/v
print('Reynolds number is', Re)

#Bragg's Law
d = 0.030
angle = radians(35)
n = 1
wave = (2*d*sin(angle))/n
print('Wavelength is', wave, 'nm')

#Arps equation
q_in = 100
Di = 2
b = 0.8
t = 10
denom = pow((1 + b*Di*t),(1/b))
q_rate = q_in/denom
#can establish multiple equations to make it look cleaner
print('Production rate is', q_rate, 'barrels/day')

#Tsiolkovsky rocket equation
V_ex = 2030
m_in = 11000
m_fi = 8300
v_delta = V_ex*log(m_in/m_fi)
print('Change of velocity is', v_delta, 'm/s')