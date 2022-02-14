size = int(input('Укажите размер файла для скачивания: '))
speed = int(input('Какова скорость вашего соединения? '))

time = (size / speed)
time = int(time + 1 if int(time) < time else time)

for second in range(1, time + 1):
    downloaded = speed * second
    percents = round(downloaded / size * 100)
    if percents < 100:
        print(f"Прошло {second} сек. Скачано {downloaded} из {size} Мб ({percents}%)")
    else:
        print(f"Прошло {second} сек. Скачано {size} из {size} Мб (100%)")
