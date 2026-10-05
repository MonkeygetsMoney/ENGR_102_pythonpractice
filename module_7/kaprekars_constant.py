numbers = input('Enter a four-digit integer: ')
num = []
num.append(numbers)
result = 0

def sort_list(x):
    x.sort(reverse=True)
    big = ''.join(x)
    big = int(big)

    x.sort()
    small = ''.join(x)
    small = int(small)

    return big, small


for number in num:
        split = list(number)
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
        else:
            num.append(str(result))


print(num)
