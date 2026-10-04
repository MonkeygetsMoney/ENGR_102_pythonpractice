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

# this program computes the change
quarter = 0.25
dime = 0.10
nickel = 0.05
cent = 0.01

pay = float(input('How much did you pay? '))
cost = float(input('How much did it cost? '))

change = pay - cost

#add in TOL
TOL = 1e-9
num_quarter = change // quarter
left_over_from_quarter = change - (quarter*num_quarter) + TOL
num_dime = left_over_from_quarter // dime
left_over_from_dime = left_over_from_quarter - (dime*num_dime) + TOL
num_nickel = left_over_from_dime // nickel
left_over_from_cent = left_over_from_dime - (nickel*num_nickel) + TOL
num_cent = left_over_from_cent // cent

print(f'You received ${change:.2f} in change. That is...')
if num_quarter > 0:
    num_quarter = int(num_quarter)
    if num_quarter == 1:
        print(f'{num_quarter} quarter')
    else:
        print(f'{num_quarter} quarters')

if num_dime > 0:
    num_dime = int(num_dime)
    if num_dime == 1:
        print(f'{num_dime} dime')
    else:
        print(f'{num_dime} dimes')

if num_nickel > 0:
    num_nickel = int(num_nickel)
    if num_nickel == 1:
        print(f'{num_nickel} nickel')
    else:
        print(f'{num_nickel} nickels')

if num_cent > 0:
    num_cent = int(num_cent)
    if num_cent == 1:
        print(f'{num_cent} penny')
    else:
        print(f'{num_cent} pennies')

