x_dist = 15
y_dist = 20
x_now = 8
y_now = 10
print(f"Марсоход высадился в центре комнаты (в точке {x_now}, {y_now}).")
print(f"Размеры комнаты: {x_dist} м ширина, {y_dist} м длина.")
print('Команды управления:\n'
      '\tW - шаг на север\n'
      '\tS - шаг на юг\n'
      '\tA - шаг на запад\n'
      '\tD - шаг на восток\n'
      '\tAny other key - отключение управления\n')

while True:
    command = input(f"Марсоход находится на позиции {x_now}, {y_now},"
                    f" введите команду:\n").lower()
    if command == 'w':
        y_now += 1 if y_now < y_dist else 0
    elif command == 's':
        y_now -= 1 if y_now > 0 else 0
    elif command == 'd':
        x_now += 1 if x_now < x_dist else 0
    elif command == 'a':
        x_now -= 1 if x_now > 0 else 0
    else:
        print('Марсоход послан в самостоятельное эротическое путешествие...')
        break
