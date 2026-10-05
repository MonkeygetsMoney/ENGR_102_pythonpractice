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
    # for special cases
    if i == 6174 or i == 0:
        iteration_sum += 0
    else:
        set1 = []
        set1.append(str(i))

        for number in set1:
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
                set1.append(str(result))
                iteration_sum += (len(set1) - 1)
                break
            else:
                set1.append(str(result))

    i += 1


print(f' Kaprekar\'s routine takes {iteration_sum} total iterations for all four digit numbers')

