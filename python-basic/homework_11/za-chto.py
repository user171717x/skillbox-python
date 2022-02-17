number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
arg_1 = number_1 // number_2
arg_1 = ((arg_1 + 2) // (arg_1 + 1)) % 2
arg_2 = (arg_1 + 1) % 2
print(f"Наибольшее число: {number_1 * arg_1 + number_2 * arg_2}")

"""
max = (a + b + abs(a-b)) / 2
"""