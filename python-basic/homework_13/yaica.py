
max_danger_level = float(input('Введите максимально допустимый уровень опасности: '))

depth = 0
dang_level = depth ** 3 - 3 * depth ** 2 - 12 * depth + 10

while dang_level > max_danger_level:
    depth += 0.0001
    dang_level = depth ** 3 - 3 * depth ** 2 - 12 * depth + 10

print(f"Приблизительная глубина безопасной кладки: {round(depth, 4)} м")
