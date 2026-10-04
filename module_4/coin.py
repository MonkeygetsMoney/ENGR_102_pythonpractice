value = 3.2 - 3.0
value2 = 0.1
value3 = 3602879701896397/36028797018963968
print (value == value2)
#have to have some kind of tolerances
print(value2.as_integer_ratio())
print(value2 == value3)
print(f'{value:.17f}')
print(f'{value3:.17f}')

a = value - value3
TOL = 1e-6
if (abs(a) < TOL):
    print('success')
else:
    print('No good')