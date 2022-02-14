
while True:
    print('Введите местоположение коня:')
    current_x = int(float(input()) * 10)
    current_y = int(float(input()) * 10)
    print('Введите местоположение точки на доске:')
    target_x = int(float(input()) * 10)
    target_y = int(float(input()) * 10)
    if current_x > 10 or current_y > 10 or target_x > 10 or target_y > 10:
        print('Одна или больше из введённых координат больше размера игровой доски. Повторите ввод')
    else:
        break
print(f"Конь в клетке ({current_x}, {current_y}). "
      f"Точка в клетке ({target_x}, {target_y}).")
step = False
if abs(target_x - current_x) == 1 and abs(target_y - current_y) == 2:
    step = True
elif abs(target_x - current_x) == 2 and abs(target_y - current_y) == 1:
    step = True
print('Да, конь может ходить в эту точку.' if step else 'Нет, конь не может ходить в эту точку.')
