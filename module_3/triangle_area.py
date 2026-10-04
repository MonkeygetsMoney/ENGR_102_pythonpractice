# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: THANH PHUNG
# Section: 570
# Assignment: Lab Topic 3
# Date: 09 SEPTEMBER 2026

from math import*

# define distance formula
x_value = float(input('Enter the value of x: '))
y_value = float(input('Enter the value of y: '))

#define the sides
#(0, x_value) - (x_value + y_value, 0)
#(0, x_value) - (x_value, y_value)
#(x_value, y_value) - (x_value + y_value, 0)

#define x variables
x_diff_1 = (0 - (x_value + y_value))
x_diff_2 = (0 - x_value)
x_diff_3 = (x_value - (x_value + y_value))

x_diff_1 = pow(x_diff_1, 2)
x_diff_2 = pow(x_diff_2, 2)
x_diff_3 = pow(x_diff_3, 2)

#define y variables
y_diff_1 = x_value - 0
y_diff_2 = x_value - y_value
y_diff_3 = y_value - 0

y_diff_1 = pow(y_diff_1, 2)
y_diff_2 = pow(y_diff_2, 2)
y_diff_3 = pow(y_diff_3, 2)

#define sides
a = sqrt(x_diff_1 + y_diff_1)
b = sqrt(x_diff_2 + y_diff_2)
c = sqrt(x_diff_3 + y_diff_3)

#Heron's formula
s_value = 1/2 * (a + b + c)
area = sqrt(s_value * (s_value - a) * (s_value - b) * (s_value - c))

print(f'The area of the triangle is {area:.3f}')

