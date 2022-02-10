dim = int(input('Введите размер стороны квадрата для креста: '))

for row in range(dim):
    for col in range(dim):
        if row == col:
            print('^', end='')
        elif row == dim - col - 1:
            print('^', end='')
        else:
            print(' ', end='')
    print()
