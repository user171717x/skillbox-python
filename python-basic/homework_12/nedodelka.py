
import random


def rock_paper_scissors():
    print('Игра «Камень, ножницы, бумага»')
    cases = ['камень', 'ножницы', 'бумага']
    bot_choice = random.choice(cases)
    player_choice = input('Ваш выбор: камень, ножницы или бумага (0 - Выход)? ').lower()
    if player_choice in cases:
        print(f"Выбор бота: {bot_choice}, ваш выбор: {player_choice}, - ", end='')
    if player_choice == 'камень':
        if bot_choice == 'камень':
            print('Ничья!')
        elif bot_choice == 'ножницы':
            print('Вы победили!')
        else:
            print('Вы проиграли!')
    elif player_choice == 'ножницы':
        if bot_choice == 'ножницы':
            print('Ничья!')
        elif bot_choice == 'бумага':
            print('Вы победили!')
        else:
            print('Вы проиграли!')
    elif player_choice == 'бумага':
        if bot_choice == 'бумага':
            print('Ничья!')
        elif bot_choice == 'камень':
            print('Вы победили!')
        else:
            print('Вы проиграли!')
    else:
        pass
    print()


def guess_the_number():
    print('Игра «Угадай число»')
    number = random.randint(1, 100)
    print('Компьютер загадал число от 1 до 100, угадайте его!')
    while True:
        num_is = int(input("Введите число: "))
        if num_is > number:
            print('Число больше, чем нужно. Попробуйте ещё раз!')
        elif num_is < number:
            print('Число меньше, чем нужно. Попробуйте ещё раз!')
        else:
            print(f"Вы угадали!")
            break
    print()


def main_menu():
    while True:
        game = input('Выберите игру (1 - камень, ножницы, бумага; 2 - угадай число; другое - выход): ')
        if game == '1':
            rock_paper_scissors()
        elif game == '2':
            guess_the_number()
        else:
            break


main_menu()
