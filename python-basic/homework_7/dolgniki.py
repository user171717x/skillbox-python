count = 0
print('Введите 10 банковских номеров:')
for idx in range(10):
    number = int(input(f"{idx + 1} номер: "))
    count += 1 if ((number % 2 == 0) and (number > 0)) else 0
print(count)
