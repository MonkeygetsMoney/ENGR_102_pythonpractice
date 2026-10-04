# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: THANH PHUNG
# Section: 570
# Assignment: Lab Topic 1
# Date: 28 AUGUST 2026

# z = 0
# x = 1
# z+= x
# print(z)
# z+= 29
# print(z)
# z+= 72
# print(z)
# z+= 9999999999999898
# print(z)
# z -= 9999999999991325
# print(z)

z = 0 
x = 1
z += x
print(z) #will print 1

x = 1
y = 10
z = 0
x+=1
x+=1
y *= x
x = y
z += y
print(z) # will print 30

x = 1
y = 10
z = 0
z += x
z += x
x = y
y *= x
z += y
print(z)# will print 102

y = 10
x = y
y *= x
x = y
y *= x
x = y
y *= x
x = y
y *= x
x = y
z = 0
z += x
print(z) #will print 10^16

z = 0
y = 10
x = y
y *= x
y *= x
x = 1
x += 1
y *= x
y *= x
y *= x
z += y
#compute for 8000

y = 10
x = y
y *= x
x = 1
x += 1
y *= x
x += 1
y *= x
z += y
# compute for 600

y = 10
x += 1
x += 1
z += x
#compute for 5
#as x is 5, add here so
#dont have to reset x back to 1 later

x += 1
x += 1
y *= x
z += y
#compute for 70
print(z) #will print 8675
