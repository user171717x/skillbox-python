print('Двузначные числа, которые равны утроенному произведению своих цифр: ', end='')
for number in range(10, 100):
    num = number // 10
    ber = number % 10
    if (num * ber) * 3 == number:
        print(f"{number}", end=' ')
