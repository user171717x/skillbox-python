count = 0
while True:
    days_month = int(input('Введите количество дней в месяце: '))
    if days_month == 0:
        break
    elif not days_month % 2:
        count += 1
print(f"Месяцев с чётным количеством дней: {count}")
