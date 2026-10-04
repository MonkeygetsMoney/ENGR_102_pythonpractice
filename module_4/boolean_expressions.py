# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Jade Kim
#               Sohan Manjunath
#               Thanh Phung
#               Quang La
# Section:      570
# Assignment:   Lab 4 - Make Change
# Date:         9 15 2026

# print('Only enter True, T, or t for True or only enter False, F, or f for false')
a = input('Enter True or False for a: ')
b = input('Enter True or False for b: ')
c = input('Enter True or False for c: ')

value_a = (a == 'True' or a == 'T' or a =='t') or not(a == 'False' or a == 'F' or a == 'f')
value_b = (b == 'True' or b == 'T' or b =='t') or not(b == 'False' or b == 'F' or b == 'f')
value_c = (c == 'True' or c == 'T' or c =='t') or not(c == 'False' or c == 'F' or c == 'f')

final = (value_a and not(value_b or value_c)) or (value_b and not(value_a or value_c)) or (value_c and not(value_a or value_b)) or (value_a and value_b and value_c)

print( f'a and b and c: {value_a and value_b and value_c}')
print( f'a or b or c: {value_a or value_b or value_c}')
print( f'XOR: {not(value_a == value_b)}')
print( f'''Odd number: {final}''')