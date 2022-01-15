sum_pos = 0
sum_neg = 0
while True:
    number = int(input('Введите число: '))
    if number > 0:
        sum_pos += 1
    elif number < 0:
        sum_neg += 1
    else:
        print(f"Кол-во положительных чисел: {sum_pos}")
        print(f"Кол-во отрицательных чисел: {sum_neg}")
        break
