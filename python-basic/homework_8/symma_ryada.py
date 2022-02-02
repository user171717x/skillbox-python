n = int(input('Введите натуральное число n: '))
s = 0
for number in range(n + 1):
    s += 1 if number == 0 else (-1) ** number * (1 / 2 ** number)
print(f"Сумма ряда S = {s}")
