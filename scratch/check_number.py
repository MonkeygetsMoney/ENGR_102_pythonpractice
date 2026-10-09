for i in range (4):
    num_2 = []

    for j in range(10):
        num = (i+2) * (j+1)
        num_2.append(str(num))

    table_2 = ', '.join(num_2)
    print(table_2)

age_old = float(input('Enter a numbers: '))
age_new = 0
age_max = 0
age_min = age_old
total = 0
count = 1
if age_old >= 0:
    while True:
        age_new = float(input('Enter a numbers: '))
        if age_new < 0.0:
            break
        if age_new > age_max:
            age_max = age_new
        elif age_new < age_min and age_new < age_max:
            age_new = age_min

        total += age_new
        count += 1

print(f'Max: {age_max}, min: {age_min}, avergae:{total/count}')