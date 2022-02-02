boys = int(input('Введите количество мальчиков: '))
girls = int(input('Введите количество девочек: '))


if boys > 2 * girls or girls > 2 * boys:
    print('Ответ: Нет решения')
elif boys > girls:
    difference = boys - girls
    print(f"{'BGB' * difference}{'BG' * (girls - difference)}")
else:
    difference = girls - boys
    print(f"{'GBG' * difference}{'GB' * (boys - difference)}")

