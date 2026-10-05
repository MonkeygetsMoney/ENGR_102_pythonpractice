name = input('What is your name? ')
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