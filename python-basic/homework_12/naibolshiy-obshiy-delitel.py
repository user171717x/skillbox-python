

def nod_inner(big_num, small_num):
    delimiter = small_num
    base = big_num
    while True:
        remainder = base % delimiter
        base = delimiter
        if remainder == 0:
            break
        delimiter = remainder
    print(f"Наибольший общий делитель НОД({big_num}, {small_num}): {delimiter}")


def nod_outer(number_1, number_2):
    if number_1 > number_2:
        nod_inner(number_1, number_2)
    else:
        nod_inner(number_2, number_1)


nod_outer(int(input('Введите первое число: ')), int(input('Введите второе число: ')))
