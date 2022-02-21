number = input('Экспоненциальная форма числа: ')
significand = float(number[:number.index('e')])
exponent = int(number[number.index('e') + 1:])

print(f"Число {number} имеет мантиссу {significand} и порядок {exponent}")
