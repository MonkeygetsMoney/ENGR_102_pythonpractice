# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Jade Kim
#               Sohan Manjunath
#               Thanh Phung
#               Quang La
# Section:      570
# Assignment:   Lab 2
# Date:         27 8 2026

#part 1
#I set the initial time (t0) at 10 minutes and the second time (t2) at 55 minutes.
t0 = 10
t2 = 55

#This is to set the location at those specific points. 
# The point x0 corresponds to the time t0 and t2 to x2
x0 = 2030
x2 = 23030

#this is to calculate the slope at which x is changing over time. (Change in x over change in time equation)
slope = (x2-x0)/(t2-t0)

#assign a time to the variable t1 (the time we want to measure x at)
# multiply the slope by the change in time (this is linear) and add the initial position
t1 = 25
x1 = slope*(t1-t0)+x0

#printing the value we found (this is formatted like the github file)
print("Part 1:")
print("For t = 25 minutes, the position p =",x1,"kilometers")

#part 2
#My plan here is to find the circumference of the path
#Basically, the distance from houston resets to 0 each time it gets there
#We can use modulo so we just get the reminder of total distance divided by that circumference
# for example, if we have passed houston twice, the code has divided by the distance twice and just gives us the reminder (distance away from Houston)

#restating the code from above
t0 = 10
t2 = 55
x0 = 2030
x2 = 23030
slope = (x2-x0)/(t2-t0)

#finding the circumference
from math import *
radius = 6745
circumference = pi*radius*2

#we're assigning the new time we need as t3; x3 is the position away from Houston at t3
t3 = 300
x3 = (slope*(t3-t0)+x0)%circumference
print("Part 2:")
print("For t = 300 minutes, the position p =",x3,"kilometers")