import math

steps = int(input('Введите кол-во чисел: '))

for _ in range(steps):
    number = float(input('Введите число: '))
    if number > 0:
        number = math.ceil(number)
        print(f"x = {number}\tlog(x) = {math.log(number)}")
    else:
        number = math.floor(number)
        print(f"x = {number}\texp(x) = {math.exp(number)}")





# import math
#
# steps = int(input('Введите кол-во чисел: '))
#
# for _ in range(steps):
#     number = float(input('Введите число: '))
#     if number > 0:
#         if int((number - int(number)) * 100) == 0:
#             number = int(number)
#         else:
#             number = int(number) + 1
#         print(f"x = {number}\tlog(x) = {math.log(number)}")
#     else:
#         if int((number - int(number)) * 100) == 0:
#             number = int(number)
#         else:
#             number = int(number) - 1
#         print(f"x = {number}\texp(x) = {math.exp(number)}")
