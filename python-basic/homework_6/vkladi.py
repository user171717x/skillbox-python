vklad = int(input("Размер вклада: "))
percent = int(input('Проценты по вкладу: '))
target = int(input('Целевая сумма: '))
years = 0
while target > vklad:
    vklad += vklad * percent // 100
    years += 1
print(f"На {years}-ый год будет достигнута целевая сумма!")
