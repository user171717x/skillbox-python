text = input('Введите текст: ') + ' '
max_len = 0
count = 0

for symbol in text:
    if symbol == ' ':
        max_len = max_len if max_len > count else count
        count = 0
    else:
        count += 1

print(f"Самое длинное слово, букв: {max_len}")
