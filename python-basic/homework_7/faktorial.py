number = int(input('Введите число: '))
factorial = 1
for idx in range(1, number + 1):
    factorial *= idx
print(f"Факториал числа {number} равен {factorial}")
