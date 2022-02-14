
print("Quadratic equation have view: (a * x^2) + (b * x) + (c) = 0, where a =/= 0")
a = float(input('Enter a number: '))
b = float(input('Enter b number: '))
c = float(input('Enter c number: '))
print(f"Quadratic equation: ({a} * x^2) + ({b} * x) + ({c}) = 0")
if c == 0:
    if b == 0:
        print("Quadratic root for the equation: x = 0")
    else:
        print(f"Quadratic roots for the equation: x = 0, x = {round(-b/a, 2)}")
elif b == 0:
    if -c/a > 0:
        if c < 0:
            c *= -1
        print(f"Quadratic roots for the equation: x = {round((c/a)**(1/2), 2)}, x = {round(-((c/a)**(1/2)), 2)}")
    else:
        print("The equation in the set of real number has no solutions")
else:
    d = b * b - 4 * a * c
    if d > 0:
        print(f"Quadratic roots for the equation: x = {round((-b+(d**(1/2)))/(2*a), 2)}, x = {round((-b-(d**(1/2)))/(2*a), 2)}")
    elif d == 0:
        print(f"Quadratic root for the equation: x = {round(-b / (2*a))}")
    else:
        print("The equation has no solution")
