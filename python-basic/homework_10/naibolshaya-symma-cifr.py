print('Введите последовательность натуральных чисел (0 - конец последовательности): ')
max_sum = 0
max_numb = None
while True:
    number = input('Введите число: ')
    if number == '0':
        break
    summ = 0
    for symbol in number:
        summ += int(symbol)
    if summ > max_sum:
        max_sum = summ
        max_numb = number
print(f"Из введённых чисел, число {max_numb} имеет наибольшую сумму цифр: {max_sum}")
