
def count_letters(text: str, number: str, symbol: str) -> None:
    print(f"Количество цифр {number}: {text.count(number)}")
    print(f"Количество букв {symbol}: {text.count(symbol)}")


count_letters(input('Введите текст: '), input('Какую цифру ищем? '), input('Какую букву ищем? '))
