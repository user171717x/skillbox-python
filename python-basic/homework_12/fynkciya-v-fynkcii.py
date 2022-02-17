def test():
    if int(input('Введите целое число: ')) >= 0:
        positive()
    else:
        negative()


def positive():
    print('Положительное')


def negative():
    print('Отрицательное')


test()
