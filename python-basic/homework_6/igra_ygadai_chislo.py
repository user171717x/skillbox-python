number = int(input("Папка загадай число: "))
tried = 0
while True:
    num_is = int(input("Введите число: "))
    tried += 1
    if num_is > number:
        print('Число больше, чем нужно. Попробуйте ещё раз!')
    elif num_is < number:
        print('Число меньше, чем нужно. Попробуйте ещё раз!')
    else:
        print(f"Вы угадали! Число попыток: {tried}")
        break
