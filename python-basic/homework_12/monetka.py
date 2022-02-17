
def is_found(point_x: float, point_y: float) -> None:
    if (-1 <= point_x <= 1) and (-1 <= point_y <= 1):
        print('Монетка где-то рядом')
    else:
        print('Монетки в области нет')


is_found(float(input('X координата точки: ')), float(input('Y координата точки: ')))
