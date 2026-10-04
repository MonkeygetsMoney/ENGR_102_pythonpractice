number = float(input('Enter your three-digit integer: '))

hundreds = number // 100
tens_ones = number % 100
tens = tens_ones // 10
ones = tens_ones % 10
addition = hundreds + tens + ones
multiply = hundreds * tens * ones
sum_product = addition * multiply

if sum_product == number:
    print(f'{number} is a sum-product')