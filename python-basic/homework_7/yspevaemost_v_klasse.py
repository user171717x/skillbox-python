pupils = int(input('В классе учеников: '))

mark_3 = 0
mark_4 = 0
mark_5 = 0
for pupil in range(pupils):
    mark = int(input(f"Введите оценку {pupil + 1}го ученика: "))
    if mark == 3:
        mark_3 += 1
    elif mark == 4:
        mark_4 += 1
    else:
        mark_5 += 1

print('Сегодня больше', end=' ')
if mark_3 > mark_4:
    if mark_3 > mark_5:
        print('троечников')
    else:
        print('отличников')
else:
    if mark_4 > mark_5:
        print('хорошистов')
    else:
        print('отличников')
