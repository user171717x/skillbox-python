

def e_convert():
    number = float(input('Введите число X > 0: '))
    length = len(str(number))
    count = 0
    if number > 0 and number > 1:
        while 10 < number:
            number /= 10
            count += 1
    elif 0 < number < 1:
        while number < 1:
            number *= 10
            count += 1
        count = -count
    else:
        e_convert()
    print(f"Формат плавающей точки: x = {round(number, length)} * 10 ** {count}")


e_convert()
