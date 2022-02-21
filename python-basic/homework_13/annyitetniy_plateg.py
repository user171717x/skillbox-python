
total_credit = float(input('Введите сумму кредита: '))
total_years = int(input('На сколько лет выдан? '))
annual_percent = float(input('Сколько процентов годовых? ')) / 100
print()

for year in range(3):
    print(f"Период: {year + 1}")
    print(f"Остаток долга на начало периода: {round(total_credit, 2)}")
    percent_paid = round(total_credit * annual_percent, 2)
    print(f"Выплачено процентов: {round(percent_paid, 2)}")
    credit_paid = ((annual_percent * (1 + annual_percent) ** total_years) * total_credit /
                   ((1 + annual_percent) ** total_years - 1) - percent_paid)
    print(f"Выплачено тела кредита: {round(credit_paid, 2)}")
    total_credit -= credit_paid
    total_years -= 1
    print()

print(f"Остаток долга: {round(total_credit, 2)}\n\n\n====================\n")

total_years += int(input('На сколько лет продлевается договор? '))
annual_percent = float(input('Увеличение ставки до: ')) / 100
print()

for year in range(total_years):
    print(f"Период: {year + 1}")
    print(f"Остаток долга на начало периода: {round(total_credit, 2)}")
    percent_paid = total_credit * annual_percent
    print(f"Выплачено процентов: {round(percent_paid, 2)}")
    credit_paid = ((annual_percent * (1 + annual_percent) ** total_years) * total_credit /
                   ((1 + annual_percent) ** total_years - 1) - percent_paid)
    print(f"Выплачено тела кредита: {round(credit_paid, 2)}")
    total_credit -= credit_paid
    total_years -= 1
    print()

print(f"Остаток долга: {round(total_credit, 2)}")
