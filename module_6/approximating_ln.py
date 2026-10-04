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

n = 0
natural_log = 0
x = float(input('Enter a value for x: '))
# global variable (I use it as an desperate attempt)
a = 1

while True:
    # detect if x in range
    if x > 0 and x <= 2:
        tol = float(input('Enter the tolerance: '))
        while a != 0:
            n += 1
            term = pow(x-1, n)/n
            if abs(term) < tol:
                a = 0
            elif n % 2 == 1:
                natural_log += term
            elif n % 2 == 0:
                natural_log -= term
        break
    else:
        x = float(input('Out of range! Try again: '))

diff = abs(natural_log - log(x))

print(f'ln({x}) is approximately {float(natural_log)}')
print(f'ln({x}) is exactly {log(x)}')
print(f'The difference is {diff}')

