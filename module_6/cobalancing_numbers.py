# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: THANH PHUNG
# Section: 570
# Assignment: Lab Topic 6
# Date: 29 SEPTEMBER 2026

fat = int(input('Enter a value for n: '))
result = 0
result2 = 0
count = 0

# sum of the first iteration
for i in range(1, (fat+1), 1):
    result += i

# sum of second iteration
while True:
    
    count +=1
    result2 += (fat + count)

    if result2 == result:
        statement = f'{fat} is a co-balancing number with r={count}'
        break
    elif result2 > result:
        statement = f'{fat} is not a co-balancing number'
        break


print(statement)