

def sign(numb):
    res = 1
    for number in range(1, numb + 1):
        res *= -1
    return res


def numerator(numb, base):
    res = base
    for number in range(1, 2 * numb):
        res *= base
    return res


def divider(numb):
    res = 1
    for number in range(1, 2 * numb + 1):
        res *= number
    return res


precision = float(input('Введите точность: '))
number_x = float(input('Введите x: '))

n = 0
addMember = 1
result = addMember

while addMember * sign(n) > precision:
    n += 1
    addMember = sign(n) * numerator(n, number_x) / divider(n)
    result += addMember

print(f"Сумма ряда = {result}")
