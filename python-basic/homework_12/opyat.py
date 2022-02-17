

def find_min_number(number_1: int, number_2: int) -> int:
    arg_1 = number_1 // number_2
    arg_1 = ((arg_1 + 2) // (arg_1 + 1)) % 2
    arg_2 = (arg_1 + 1) % 2
    return number_1 * arg_2 + number_2 * arg_1


print(f"Меньшее число: {find_min_number(int(input('Введите первое число: ')), int(input('Введите второе число: ')))}")
