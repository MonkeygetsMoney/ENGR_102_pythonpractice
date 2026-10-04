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

a = int(float(input('Please enter the coefficient A: ')))
b = int(float(input('Please enter the coefficient B: ')))
c = int(float(input('Please enter the coefficient C: ')))

# define equation as a string
equation = ''

#detect zero when input
if a == 0 and b != 0 and c != 0:
    A = ''
    if b > 0:
        if b == 1:
            B = 'x' 
        else:
            B = f'{b}x'
    else:
        B = f' - {b}x'

    if c > 0:
        C = f' + {c}'
    elif c < 0:
        c = c*-1
        C = f' - {c}'
    elif c == 0:
        C = ''

elif b == 0 and a != 0 and c != 0:
    B = ''
    if a == 0:
        A = ''
    elif a < 0:
        a = a * -1
        if a == 1:
            A = f'- x^2'
        else:
            A = f'- {a}x^2'
    elif a > 0:
        if a == 1:
            A = f'x^2'
        else:
            A = f'{a}x^2'

    if c > 0:
        C = f' + {c}'
    elif c < 0:
        c = c*-1
        C = f' - {c}'
    elif c == 0:
        C = ''

elif c == 0 and a != 0 and b != 0:
    C = ''
    if a == 0:
        A = ''
    elif a < 0:
        a = a * -1
        if a == 1:
            A = f'- x^2'
        else:
            A = f'- {a}x^2'
    elif a > 0:
        if a == 1:
            A = f'x^2'
        else:
            A = f'{a}x^2'

    if b > 0:
        if b == 1:
            B = 'x'
        else:
            B = f' + {b}x'
    elif b < 0:
        b = b *-1
        B = f' - {b}x'
    elif b == 0:
        B = ''

elif a == 0 and b == 0 and c != 0:
    A = ''
    B = ''
    if c == 0:
        C = ''
    elif c > 0:
        C = f'{c}'
    elif c < 0:
        c = c*-1
        C = f' - {c}'

elif a == 0 and c == 0 and b != 0:
    A = ''
    C = ''
    if b == 1:
        B = 'x'
    elif b > 0:
        B = f'{b}x'
    elif b < 0:
        b = b *-1
        B = f' - {b}x'

elif c == 0 and b == 0 and a != 0:
    C = ''
    B = ''
    if a == 1:
        A = f'x^2'
    elif a < 0:
        a = a*-1
        A = f' - {a}x^2'
    elif a > 0:
        A = f'{a}x^2'


equation = f'{A}{B}{C} = 0'
print(f'The quadratic equation is {equation}')