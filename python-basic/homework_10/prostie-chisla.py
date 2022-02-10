print('Введите последовательность целых положительных чисел (0 - конец последовательности): ')
summ = 0
while True:
    number = int(input('Введите число: '))
    if number == 0:
        break
    deviders = 0
    for numb in range(1, number + 1):
        if number % numb == 0:
            deviders += 1
    if deviders < 3:
        summ += 1
print(f"Количество простых чисел в последовательности: {summ}")
