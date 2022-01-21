max_number = int(input('Номер наибольшей карточки: '))
total = 0
for number in range(1, max_number + 1):
    total += number
for number in range(1, max_number):
    total -= int(input('Введите номер одной из оставшихся карточек: '))
print(f"Номер потерянной карточки: {total}")
