call = False
hour = 1
tasks = 0
print('Начался 8-часовой рабочий день')
while hour < 9:
    print(f"{hour}-й час")
    tasks += int(input('Сколько задач решит Максим? '))
    if int(input('Звонит жена. Взять трубку? (1 — да, 0 — нет): ')):
        call = True
    hour += 1
print(f"Рабочий день закончился. Всего выполнено задач: {tasks}")
if call:
    print('Нужно зайти в магазин.')
