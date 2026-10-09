phone = input('Enter a phone number in this format XXX-XXXXXXX: ')
a = []
b = ['X', 'x', 'x','x','x','x','x','x','x','x']
words = [['A','B','C'], ('DEF'), ('GHI'), ('JKL'), ('MNO'), ('PQRS'), ('TUV'), ('WXYZ')]
nums = '012346789'
for i in phone:
    if i == '-':
        continue
    else:
        a.append(i)

for index, character in enumerate(a):
    for i in range(len(words)):
        for j in range(len(words[i])):
            if character == words[i][j]:
                num = str(i+2)
                b[index] = num
            else: continue

print(b)
