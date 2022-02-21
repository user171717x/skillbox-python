
def fluctuations():
    start = float(input('Введите начальную амплитуду: '))
    finish = float(input('Введите амплитуду остановки: '))

    if start > finish:
        count = 0

        while start > finish:
            start *= 0.916
            count += 1

        print(f"Маятник считается остановившимся через {count} колебаний")
    else:
        print('Амплитуда начальных колебаний должна быть больше амплитуды конечных колебаний!\n')
        fluctuations()


fluctuations()
