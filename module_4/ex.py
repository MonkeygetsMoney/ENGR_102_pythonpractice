day = float(input('Please enter a positive value for day: '))

if (day == ValueError or day < 0):
    print('You entered an invalid number!')

if (day > 0 and day != ValueError):
    if (day <= 10):
        speed = 10
        produce = speed * day
    elif (day > 10 and day <=50):
        day_count = day - 11 + 1
        produce_10 = 100
        produce = day_count * (day + 11) * 1/2 + 100
    elif (day > 50 and day <= 100):
        count_after_50 = day - 50
        speed = 50 * count_after_50
        produce = 40 * (50 + 11) * 1/2 + 100 + speed
    elif(day > 100):
        produce = 3820
    print(f'The sum total number of gadgets produced on day {day:.0f} is {produce:.0f}')
            

