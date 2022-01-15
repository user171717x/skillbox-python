number = int(input("Загадай число (1 - 100): "))

left = 1
right = 101

while True:
    center = (left + right) // 2
    answer = int(input(f"Твоё число равно(1), меньше(3) или больше(2), чем число {center}?"))
    if answer == 3:
        right = center
    elif answer == 2:
        left = center
    else:
        print(f"Твоё число угадано, это: {center}")
        break
