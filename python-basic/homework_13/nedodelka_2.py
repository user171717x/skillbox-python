

def is_valid_num(number, length):
    if result := len(number) >= length:
        pass
    else:
        if length == 3:
            print('В первом числе меньше трёх цифр.')
        else:
            print('Во втором числе меньше четырёх цифр.')
    return result


def convert_num(number):
    return int(number[-1:] + number[1:-1] + number[:1])


first_n = input("Введите первое число: ")
second_n = input("Введите второе число: ")

if is_valid_num(first_n, 3) and is_valid_num(second_n, 4):
    conv_1 = convert_num(first_n)
    conv_2 = convert_num(second_n)
    print(f"Изменённое первое число: {conv_1}")
    print(f"Изменённое второе число: {conv_2}")
    print(f"Сумма изменённых чисел: {conv_1 + conv_2}")


