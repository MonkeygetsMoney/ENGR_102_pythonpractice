a = 'hello'
string = a + 'Toby Pie'
print(string)

for i in range(5):
    i = str(i) + ', '
    string += i

print(string)

num = 5 % 2
print(num)

# testing the sort method
a = [(2, 1), (2, 5), (2, 4), (2, 9), (3, 1)]
a.sort()
print(a)