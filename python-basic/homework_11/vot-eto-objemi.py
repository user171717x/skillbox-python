import math

planet_v = 4 / 3 * math.pi * float(input('Введите радиус случайной планеты: ')) ** 3
earth_v = 10.8321 * 10 ** 11
if planet_v < earth_v:
    print(f"Объём планеты Земля больше в {round(earth_v / planet_v, 3)} раз")
else:
    print(f"Объём планеты Земля меньше в {round(planet_v / earth_v, 3)} раз")
