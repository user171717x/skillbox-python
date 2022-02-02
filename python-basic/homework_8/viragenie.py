x = int(input('Введите число x: '))
res = 1
try:
    for number in range(1, 7):
        arg = 2 ** number
        res = res * (x - arg - 1) / (x - arg)
    print(f"Результат ряда res = {res}")
except ZeroDivisionError:
    print(f"Недопустимое значение х для этого выражения")
