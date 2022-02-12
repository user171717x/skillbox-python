height = int(input('Введите высоту треугольника: '))
current = 1
for row in range(0, height + 1):
    print('\t' * (height - row), end='')
    for _ in range(0, row):
        print(f"{current}\t\t", end='')
        current += 2
    print()
