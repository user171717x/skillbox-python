
def max_num(num1, num2):
    return int((num1 + num2 + abs(num1 - num2)) / 2)


number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
number_3 = int(input('Введите третье число: '))

print(f"Наибольшее число: {max_num(max_num(number_1, number_2), number_3)}")
