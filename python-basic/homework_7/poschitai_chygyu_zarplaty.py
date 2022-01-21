year_profit = 0
months_in_year = 12
print('Введите З\П за каждый из 12ти месяцев:')
for idx in range(months_in_year):
    year_profit += int(input(f"{idx + 1} месяц: "))
print(f"Средняя ежемесячная зарплата в этом году: {year_profit // months_in_year}")
