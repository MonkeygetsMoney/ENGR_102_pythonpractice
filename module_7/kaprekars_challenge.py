# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: THANH PHUNG
# Section: 570
# Assignment: Lab Topic 7
# Date: 5 OCTOBER 2026

i = 0
result = 0
string = ''
iteration_sum = 0
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

for i in range(10000): 
    set1 = []
    set1.append(str(i))
    for number in set1:
        set2 = []
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
            
        if result == 6174 or result == 0:
            set2.append(str(result))
            iteration_sum += len(set2)
            break
        else:
            set2.append(str(result))

    i += 1

for number in set1:
    if number != '6174':
        string += f'{number} > ' 
    else: 
        string += f'{number}'

print(iteration_sum)

# if result == 6174:
#     print(f'{num[0]} reaches 6174 via Kaprekar\'s routine in {len(num) - 1} iterations')
# else:
#     print(f'{num[0]} reaches 0 via Kaprekar\'s routine in {len(num) - 1} iterations')