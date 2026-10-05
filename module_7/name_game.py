# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: THANH PHUNG
# Section: 570
# Assignment: Lab Topic 7
# Date: 5 OCTOBER 2026

name = input('What is your name? ')
# define vowels
vowels = ['a', 'i', 'e', 'u', 'o', 'y', 'A', 'I', 'E', 'U', 'O', 'Y']

check = True
for i, letter in enumerate(name):
    for vowel in vowels:
        if letter == vowel:
            lowercase = name.lower()
            y = lowercase[i:]
            check = False
        else:
            continue

    if check == False:    
        break

print(f'{name}, {name}, Bo-B{y}')
print(f'Banana-Fana Fo-F{y}')
print(f'Me Mi Mo-M{y}')
print(f'{name}!')