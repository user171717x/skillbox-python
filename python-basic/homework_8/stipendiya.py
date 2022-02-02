educational_grant = int(input('Введите стипендию: '))
expenses = int(input('Введите расходы на проживание: '))

edu_monthes = 10
total_expenses = 0

for _ in range(edu_monthes):
    total_expenses += expenses
    expenses *= 1.03

print(f"У родителей необходимо попросить {round(total_expenses - educational_grant * 10, 2)}")
