total_time = int(input('Время срабатывания бомбы: '))

for moment in range(total_time, 0, -1):
    if int(input(f"До взрыва осталось {moment} сек, обезвредить бомбу сейчас(0- нет \ 1 - да)? ")):
        print(f"Бомба обезврежена за {moment} сек до взрыва!")
        break
    if moment == 1:
        print('Бомба взорвалась')
