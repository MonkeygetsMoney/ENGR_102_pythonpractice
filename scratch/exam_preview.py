# problem 1
x = 5 / 5
print(x)

x = 5 ** 5
print(x)

# problem 2
print(7 * 2 ** 3 - 12 * 2 // 7 + 8 % 3)

# problem 3
from math import *
print(f"ENGR {sqrt(625) * 4 + 2}")

# problem 4
a = 3
b = 2
c = 4
print(a * b + c // c - b)

# problem 5
x = 4
y = 8
t = x
x = y
y = t
z = x / y
print(z)

# problem 6
x = 7
y = 8
z = x + y / 4
a = (y - x) * 2
z += a
b = z // 2
c = x * 5
c %= 4
print(c)

c = bool()
print(c)

# problem 8
x = "3"
print((2 * x))

# problem 10
x = 5 % 2 == 1 and 5 < 2 + 4
print(x)

# problem 13
a = 10
b = 10
c = 20
d = a > b and b <= c
e = not(((c <= a + b and a == 10) or (b == 10 and c != 10)))
print(d or e)

# a = '5.6'
# int(a)
# print(a)
# cannot transform a 'float string' into integer

# problem 15
a = 5
b = 6
c = 7
d = float(str(a * 2)) > float(str(b + c))
e = float(str(a) * 2) >= float(str(b) + str(c)) - 11
print(d or e, 'is false')

# problem 16
a = True
b = bool("False")
c = 5 > 8
d = a and b and c
e = not a or not (b and c)
print(d, e)

# problem 17
x = "7"
y = "16"
z = 772
if x * 2 + "2" == y:
    print(y + y)
elif x * 2 + "2" == z:
    print(z + z)
    # not equal to z becasue the condition result in a string
else:
    print(x + x)

# problem 18
a = "Aitor_cruzado"
if "ai" in a:
    b = a[:-8]
elif "cr" in a:
    b = a[9:999]
print(b)

# problem 19
a = int(False) + 6
b = int("2" * 2) - 48 / 3
z = int("2" + "3")
if a == b:
    z %= 5
elif b == 6:
    z //= 5
else:
    z += 5
print(z)

# problem 20
a = 1
b = 2
c = "a"
d = int(float("3.14"))
if a == 1 and d == 3.14:
    print("Green")
elif c == a or d > 3:
    print("Red")
else:
    print("Yellow")

c = a
if c == 'a':
    print('It\'s the same')
else:
    print('It\'s not the same')

# problem 21
x = 0
y = 2
if x > 0 and y > 0:
    print("x > 0 and y > 0")
elif x > 0 or y > 0:
    if x > 0:
        print(x)
    else:
        print(y)
elif x == 0:
    print("x == 0")
else:
    print(x + y)

# problem 22
x = 10
y = 5
if x % 2 == 0:
    if y > 5:
        print("A")
    else:
        print("B")
        print("C")
else:
    if y < 5:
        print("D")
    else:
        print("E")
        print("F")
print("G")

# problem 23
a = 5
b = "b"
c = True
print("The answer is...", end=" ")
if a != 10:
    print("A", end=" ")
elif b == "b":
    print("B", end=" ")
else:
    print("C", end=" ")
z = c and bool(a)
print(z, end=" ")
d = a ** 3 + 25 % 3 - 12 // 5
print(d)

for i in range(3):
    print(i)
    i += 1

# problem 32
for i1 in range(1, 3):
    for i2 in range(i1 + 1):
        i1 += 1
        print(f"{i1}{i2}", end=" ")

        # i2 += 1
        # this doesn't do anything since the for loop will reassign

    print() # new line

thy = 'string big'
print(thy[::])

# problem 37
a = "My name is aitor"
count = 0
for i in a:
    if i == "a":
        print(a[:count+7])
        print(count)
    elif i == "i":
        break
    else:
        continue
    count += 1
    print(count)

a = -11
print(-a)

x = 3
y = 5
print(x != y - 2)
print(x >= 0 and not x < 10)
print(x < 0 and x < 10)
print(x >= 0 and x < 2)
print(x < 0 or y < 5)
print(not x > 0 or x < 10)

print(str(float(str(3 / 2) + str(int(3 / 2)))) * int(int(str(2) + str(7)) / int(10.3)))
# print(x = str(int("5 + 6"))) print out error code
_10_KG_Mass = 10
print(_10_KG_Mass)

# problem 49
a = [12, 89, 45, 12, 67, 3, 4, 9, 20, 34, 45, 67, 199, 67]
count = 0
for i in a:
    if i % 5 == 0:    # this line is different
        for j in range(len(a)):
            if i == a[j]:
                print(i, end=", ")
                continue    # these 2 lines are different
            else:
                count += 1
    else:
        count -= 1
print(count)


# problem 48
a = [12, 89, 45, 12, 67, 3, 4, 9, 20, 34, 45, 67, 199, 67]
count = 0
for i in a:
    if i % 2 == 0:
        for j in range(len(a)):
            if i == a[j]:    # this line is different
                break
            else:
                count += 1
    else:
        count -= 1
print(count, a[0:234], sep='.  ')

v = [9, 5, -3, 6, -1, 0]
print(v[-6:2])

# problem 37
a = "My name is aitor"
count = 0
for i in a:
    if i == "a":
        print(a[:count+7])
        print(count)
    elif i == "i":
        break
    else:
        continue
    count += 1
    print(count)

a = b
print(a == 'b')


