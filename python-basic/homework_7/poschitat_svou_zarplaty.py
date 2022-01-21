months = 10
previous_profit = 0
print('Введите З\П за последние 10 месяцев:')
for idx in range(months):
    current_profit = int(input(f"{idx + 1} месяц: "))
    if previous_profit < current_profit:
        previous_profit = current_profit
        if idx == months - 1:
            print('У Вас тенденция роста зарплаты!')
    else:
        print('Зарплата не растёт !')
        break
