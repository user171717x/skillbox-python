number = int(input('Введите число для образования ямы: '))
for row in range(1, number + 1):
    for idx in range(number, 0, -1):
        if number - idx < row:
            print(idx, end='')
        else:
            print('.', end='')
    for idx in range(1, number + 1):
        if number - row + 1 <= idx:
            print(idx, end='')
        else:
            print('.', end='')
    print()
