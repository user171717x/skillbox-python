danger = 0
print('Введите количество людей по секторам:')
for idx in range(30, 36):
    number = int(input(f"Людей в {idx} секторе: "))
    if number > 10:
        danger += 1
        print('Нарушение! Слишком много людей в секторе!')
    else:
        print('Всё спокойно.')
print(f"Количество нарушений: {danger}")
