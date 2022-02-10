height = int(input('Введите высоту треугольника: '))
for x in range(0, height + 1):
    for y in range(0, height - x):
        print(' ', end='')
    print('#' * (2 * x - 1))

