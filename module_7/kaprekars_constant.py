numbers = input('Enter a four-digit integer: ')
num = []
numbers = list(numbers)

for number in numbers:
    number = int(number)
    num.append(number)

num.sort()
print(num)
