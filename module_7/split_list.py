# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: THANH PHUNG
# Section: 570
# Assignment: Lab Topic 7
# Date: 5 OCTOBER 2026

numbers = input('Enter numbers: ')
numbers = numbers.split()
num = []
sum = 0

for number in numbers:
        number = int(number)
        num.append(number)

for i, number in enumerate(num):
    equal = False
    sum += number
    sum2 = 0
    for integer in num[i+1:]:
        sum2 += integer
        if integer == num[-1]:
            if sum2 == sum:
                index = i
                equal = True
            else: continue

    if equal:
        break

if equal:
    print(f'Left: {num[:i+1]}')
    print(f'Right: {num[i+1:]}')
    print(f'Both sum to {sum}')
elif not equal:
    print('Cannot split evenly')


