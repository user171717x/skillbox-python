number_a = int(input('Введите a: '))
number_b = int(input('Введите b: '))
number_c = int(input('Введите c: '))

total = 0
count = 0
for number in range(number_a, number_b + 1):
    if (number != 0) and (number % number_c == 0):
        total += number
        count += 1
print(f"Среднее арифметическое всех чисел из отрезка [{number_a}; {number_b}], кратных числу {number_c}: {total // count}")
