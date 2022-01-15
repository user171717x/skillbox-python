number = int(input('Введите число для подсчёта его длины: '))
length = 0
if number == 0:
    print('Количество цифр в числе: 1')
else:
    while number > 0:
        number //= 10
        length += 1
    print(f"Количество цифр в числе: {length}")
