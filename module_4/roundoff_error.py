# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Jade Kim
#               Sohan Manjunath
#               Thanh Phung
#               Quang La
# Section:      570
# Assignment:   Lab 4 - Make Change
# Date:         9 15 2026

############ Part A ############
a = 1 / 7
print(f'a = {a}')
b = a * 7
print(f'b = a * 7 = {b}')

# whether if there's round off or not
# the result still equal 1 because
# we multiply the denominator by itself 
# so it cancel out

c = 2 * a
d = 5 * a
f = c + d
print(f'f = 2 * a + 5 * a = {f}')

# Yes without roundoff, the value of f should be 1

from math import*
x = sqrt(1/3)
print(f'x = {x}')
y = x * x * 3
print(f'y = x * x * 3 = {y}')
z = x * 3 * x
print(f'z = x * 3 * x = {z}')

# if there no roundoff, values of both y and z would be 1
# since there round off, only y = 1.0

############ Part B ############
TOL = 1e-10
if abs(b-f) < TOL:
    print(f'b and f are equal within tolerance of {TOL}')
else:
    print(f'b and f are NOT equal within tolerance of {TOL}')

if abs(y-z) < TOL:
    print(f'y and z are equal within tolerance of {TOL}')
else:
    print(f'y and z are NOT equal within tolerance of {TOL}')

############ Part c ############
m = 0.1
print(f'm = {m}')
n = 3 * m
print(f'n = 3 * m = 0.3 {n == 0.3}')
p = 7 * m
print(f'p = 7 * m = 0.7 {p == 0.7}')
q = n + p
print(f'q = n + p = 1 {q == 1}')

# Yes, the result does surprise me
# although n and p get the desired results
# boolean operation still output wrong

# the reason for why n and p still output 
# boolean wrong had to do with how float is represented
# 0.1 is not exactly 0.1 with 0 follow behind
# 0.1 represent in machine is 
# 0.1000000000000000055511151231257827021181583404541015625
#therefore, that's why although number look equal
#python just cut off the decimals so it looks desirable
# to see actual decimal, we can use the method float.as_integer_ratio()
