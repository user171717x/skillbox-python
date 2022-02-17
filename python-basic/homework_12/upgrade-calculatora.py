
def numbers_sum(numb: int):
    print(f"Сумма цифр данного числа: {sum(convert(numb))}\n")


def max_number(numb: int):
    print(f"Максимальная цифра данного числа: {max(convert(numb))}\n")


def min_number(numb: int):
    print(f"Минимальная цифра данного числа: {min(convert(numb))}\n")


def convert(numb: int):
    return [int(symbol) for symbol in str(abs(numb))]


while True:
    print('Выберите действие:\n1) Сумма цифр числа\n2) Максимальная цифра данного числа\n'
          '3) Минимальная цифра числа\n0) Завершение работы')
    todo = int(input())
    if todo == 0:
        break
    number = int(input('Введите число для вычислений: '))
    if todo == 1:
        numbers_sum(number)
    elif todo == 2:
        max_number(number)
    elif todo == 3:
        min_number(number)
    else:
        break
