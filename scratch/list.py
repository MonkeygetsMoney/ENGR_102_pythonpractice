name = 'Toby Pie'
letter = []

for character in name:
    if character == ' ':
        continue

    letter.append(character)

print(name[1:])