input1 = input('User 1 please enter a birthday: ')
input1 = input1.split()

input2 = input('User 2 please enter a birthday: ')
input2 = input2.split()

input3 = input('User 3 please enter a birthday: ')
input3 = input3.split()

# input4 = input('User 4 please enter a birthday: ')
# input4 = input4.split()

# input5 = input('User 5 please enter a birthday: ')
# input5 = input5.split()

# define month to loop over
months = ['January', 'February', 'March', 'April', 'May', 'June', 
         'July', 'August', 'September', 'October', 'November', 'December']

month_enter = []
date_enter = []

month_enter.append(input1) # append only take one agrument
month_enter.append(input2)
month_enter.append(input3)



month_sorted = []

for month in months:
    for birth_month in month_enter:
        if birth_month == month:
            birthdate = birth_month
            month_sorted.append(birthdate)
    else: continue


print(month_sorted)