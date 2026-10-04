# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: THANH PHUNG
# Section: 570
# Assignment: Lab Topic 1
# Date: 28 AUGUST 2026

#this program will use interpolation formula 
#to calculate an unknown point
#given initial and final point

from math import*

t1 = 12
t2 = 85
x1 = 8
y1 = 6
z1 = 7
x2 = -5
y2 = 30
z2 = 9

t_denom = t2 - t1 
#this can be used to calculated

x_slope = (x2 - x1)/t_denom
y_slope = (y2 - y1)/t_denom
z_slope = (z2 - z1)/t_denom

t_dist = 30 - 12
x_cal = x_slope*t_dist + x1
y_cal = y_slope*t_dist + y1
z_cal = z_slope*t_dist + z1
print('At time 30.0 seconds:')
print('x1 =', x_cal, 'm')
print('y1 =', y_cal, 'm')
print('z1 =', z_cal, 'm')
print('-----------------------')

t_dist = 37.5 - 12
x_cal = x_slope*t_dist + x1
y_cal = y_slope*t_dist + y1
z_cal = z_slope*t_dist + z1
print('At time 37.5 seconds:')
print('x2 =', x_cal, 'm')
print('y2 =', y_cal, 'm')
print('z2 =', z_cal, 'm')
print('-----------------------')

t_dist = 45 - 12
x_cal = x_slope*t_dist + x1
y_cal = y_slope*t_dist + y1
z_cal = z_slope*t_dist + z1
print('At time 45.0 seconds:')
print('x3 =', x_cal, 'm')
print('y3 =', y_cal, 'm')
print('z3 =', z_cal, 'm')
print('-----------------------')

t_dist = 52.5 - 12
x_cal = x_slope*t_dist + x1
y_cal = y_slope*t_dist + y1
z_cal = z_slope*t_dist + z1
print('At time 52.5 seconds:')
print('x4 =', x_cal, 'm')
print('y4 =', y_cal, 'm')
print('z4 =', z_cal, 'm')
print('-----------------------')

t_dist = 60 - 12
x_cal = x_slope*t_dist + x1
y_cal = y_slope*t_dist + y1
z_cal = z_slope*t_dist + z1
print('At time 60.0 seconds:')
print('x5 =', x_cal, 'm')
print('y5 =', y_cal, 'm')
print('z5 =', z_cal, 'm')
print('-----------------------')
