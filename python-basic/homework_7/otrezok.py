number_a = int(input('Введите число a: '))
number_b = int(input('Введите число b: '))

total_sum = 0
total_count = 0
for number in range(number_a, number_b + 1):
    if number % 3 == 0:
        total_count += 1
        total_sum += number
print(f"Среднее арифметическое всех чисел из отрезка [{number_a}; {number_b}],"
      f" кратных числу 3: {total_sum // total_count}")
