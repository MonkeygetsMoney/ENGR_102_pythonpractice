input1 = input('User 1 please enter a birthday: ')
input1 = input1.split()

input2 = input('User 2 please enter a birthday: ')
input2 = input2.split()

input3 = input('User 3 please enter a birthday: ')
input3 = input3.split()

input4 = input('User 4 please enter a birthday: ')
input4 = input4.split()

input5 = input('User 5 please enter a birthday: ')
input5 = input5.split()

# define month to loop over
months = ['January', 'February', 'March', 'April', 'May', 'June', 
         'July', 'August', 'September', 'October', 'November', 'December']

month_enter = []

month_enter.append(input1) # append only take one agrument
month_enter.append(input2)
month_enter.append(input3)
month_enter.append(input4)
month_enter.append(input5)

month_sorted = []

for birth_month, date in month_enter:
    for i in range(len(months)):
        if months[i] == birth_month:
            date = int(date)
            birthdate = i, date
            month_sorted.append(birthdate)
        else: 
            continue

month_sorted.sort()

month_date_sort = []
for i in range(len(month_sorted)):
    month = month_sorted[i][0]
    month = months[month], month_sorted[i][1]
    month_date_sort.append(month)

print(month_date_sort)