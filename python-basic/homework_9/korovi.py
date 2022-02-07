scheme = input('Введите схему расположения коров (a - свободно, b - занято): ')
total_milk = 0
for idx in range(10):
    total_milk += 2 * (idx + 1) if scheme[idx] == 'b' else 0
print(total_milk)
