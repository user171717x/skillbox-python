
summ = 0
for number in range(1, int(input('Введите число N: ')) + 1):
    mult = 1
    for numb in range(1, number + 1):
        mult *= numb
    summ += mult
print(f"Сумма факториалов: {summ}")
