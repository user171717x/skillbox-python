number = int(input('Введите номер билета (6 цифр): '))
idx = 100000
sum_l = 0
sum_r = 0
while idx >= 1:
    if idx > 100:
        sum_l += (number // idx) % 10
    else:
        sum_r += (number // idx) % 10
    idx /= 10
if sum_l == sum_r:
    print('Билет счастливый!')
else:
    print('Билет обычный.')
