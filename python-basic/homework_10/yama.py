number = int(input('Введите число для образования ямы: '))
for row in range(1, number + 1):
    for idx in range(number, 0, -1):
        if number - idx < row:
            print(idx, end='')
        else:
            print('.', end='')
    for idx in range(1, number + 1):
        if number - row + 1 <= idx:
            print(idx, end='')
        else:
            print('.', end='')
    print()

# depth = int(input('Введите число для образования ямы: '))
# for line in range(depth):
#     for left_number in range(depth, depth - line - 1, -1):
#         print(left_number, end='')
#     point_count = 2 * (depth - line -1)
#     print('.' * point_count, end='')
#     for right_number in range(depth - line, depth + 1):
#         print(right_number, end='')
#     print()
