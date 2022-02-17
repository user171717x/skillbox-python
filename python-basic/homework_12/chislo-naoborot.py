
def reverse(numb: int):
    print(f"Число наоборот: {int(str(numb)[::-1])}")


while True:
    number = int(input('Введите число: '))
    if number == 0:
        print('Программа завершена!')
        break
    else:
        reverse(number)
