print('Ввод:')
while True:
    lower = int(input('Нижняя граница(celsium): '))
    upper = int(input('Верхняя граница(celsium): '))
    if upper < lower:
        print('Верхняя граница температуры должна быть выше нижней границы. Повторите ввод')
    else:
        break
step = int(input('Шаг(celsium): '))
print('Вывод:\nC\tF')
for temp in range(lower, upper + 1):
    if not(temp % step) or temp == lower or temp == upper:
        print(f"{temp}\t{round(32 + temp * 1.8)}")
