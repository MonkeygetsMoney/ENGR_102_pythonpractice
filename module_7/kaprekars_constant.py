# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: THANH PHUNG
# Section: 570
# Assignment: Lab Topic 7
# Date: 5 OCTOBER 2026

numbers = input('Enter a four-digit integer: ')
num = []
num.append(numbers)

result = 0
string = ''
# def sort_list(x):
#     x.sort(reverse=True)
#     big = ''.join(x)
#     big = int(big)

#     x.sort()
#     small = ''.join(x)
#     small = int(small)

#     return big, small
# can always use this function to make the program simpler 
# but this can be for reference

for number in num:
    split = list(number)
    while len(split) != 4:
        split.append('0')

    split.sort(reverse=True)
    big = ''.join(split)
    big = int(big)

    split.sort()
    small = ''.join(split)
    small = int(small)
    result = big - small
        
    if result == 6174:
        num.append(str(result))
        break
    elif result == 0:
        num.append(str(result))
        break
    else:
        num.append(str(result))


for number in num:
    if number != '6174':
        string += f'{number} > ' 
    else: 
        string += f'{number}'

print(string)

if result == 6174:
    print(f'{num[0]} reaches 6174 via Kaprekar\'s routine in {len(num) - 1} iterations')
else:
    print(f'{num[0]} reaches 0 via Kaprekar\'s routine in {len(num) - 1} iterations')