# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: THANH PHUNG
# Section: 570
# Assignment: Lab Topic 5
# Date: 21 SEPTEMBER 2026

from math import *

sex = input('Enter your sex (M/F): ')
age = float(input('Enter your age (years): '))
BMI = float(input('Enter your BMI: '))
hypertension_med = input('Are you on medication for hypertension (Y/N)? ')
steroids = input('Are you on steroids (Y/N)? ')
smoke = input('Do you smoke cigarettes (Y/N)? ')
if smoke == 'y' or smoke == 'Y':
        smoker = 0.855
elif smoke == 'n' or smoke == 'N':
    smoked = input('Did you used to smoke (Y/N)? ')
    if smoked == 'y' or smoked == 'Y':
        smoker = - 0.218
    elif smoked == 'n' or smoked == 'N':
        smoker = 0
history = input('Do you have a family history of diabetes (Y/N)? ')

# don't put in bracket because python check individually after each boolean operators
if history == 'y' or history == 'Y' or history == 'yes' or history == 'Yes':
    family = input('Both parent and sibling (Y/N)? ')

    if family == 'y' or family == 'Y' or family == 'yes' or family == 'Yes':
        family_value = 0.753
    elif family == 'n' or family == 'N' or family == 'no' or family == 'No':
        family_value = 0.728
elif history == 'n' or history == 'N' or history == 'no' or history == 'No':
        family_value = 0
else:
    family_value = 0

if sex == 'F' or sex == 'f':
    sex = 6.322 + 0.879
elif sex == 'M' or sex == 'm':
    sex = 6.322 + 0

if BMI > 0:
    if BMI < 25:
        BMI_value = 0
    elif BMI >= 25 and BMI <= 27.49:
        BMI_value = 0.699
    elif BMI >= 27.5 and BMI <= 29.99:
        BMI_value = 1.97
    elif BMI >= 30:
        BMI_value = 2.518

if hypertension_med == 'y' or hypertension_med == 'Y' or hypertension_med == 'yes' or hypertension_med == 'Yes':
    med = 1.222
elif hypertension_med == 'no' or hypertension_med == 'No' or hypertension_med == 'n' or hypertension_med == 'N':
    med = 0

if steroids == 'y' or steroids == 'Y':
    steroids = 2.191
elif steroids == 'n' or steroids == 'N':
    steroids = 0
    
n = sex - (0.063 * age) - BMI_value - med - steroids - smoker - family_value
risk = 100 / (1 + pow(e, n))
print(f'Your risk of developing type-2 diabetes is {risk:.1f}%')