rows = int(input('Введите кол-во рядов: '))
sites = int(input('Введите кол-во сидений в ряде: '))
distance = int(input('Введите кол-во метров между рядами: '))

print('\nСцена\n')
print(f"{'=' * sites} {'*' * distance} {'=' * sites}\n" * rows, end='')
