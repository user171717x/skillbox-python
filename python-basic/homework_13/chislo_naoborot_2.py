
def reverse(numb):
    return int(str(numb)[::-1])


number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))

rev_1 = reverse(number_1)
rev_2 = reverse(number_2)
summ = rev_1 + rev_2
rev_summ = reverse(summ)

print(f"Первое число наоборот: {rev_1}")
print(f"Второе число наоборот: {rev_2}")
print(f"Сумма: {summ}")
print(f"Сумма наоборот: {rev_summ}")
