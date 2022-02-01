point_a = int(input("Введите Х точки начала отрезка: "))
point_b = int(input("Введите Х точки конца отрезка: "))
step = int(input("Введите шаг расчёта функции: "))

if step > 0:
    if point_a < point_b:
        point_start = point_a
        point_end = point_b + 1
    else:
        point_start = point_a
        point_end = point_b - 1
        step = -step
else:
    if point_a < point_b:
        point_start = point_b
        point_end = point_a - 1
    else:
        point_start = point_b
        point_end = point_a + 1
        step = -step


for point_x in range(point_start, point_end, step):
    print(f"В точке {point_x} функция равна {point_x ** 3 + 2 * point_x ** 2 - 4 * point_x + 1}")

