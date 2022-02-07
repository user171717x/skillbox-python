import re

string = input('Введите строку: ')
result = 0
count = 0
for symbol in string:
    if symbol == 's':
        count += 1
    else:
        result = result if result > count else count
        count = 0

print(f"Самая длинная последовательность: {result}")
# print(f"Самая длинная последовательность: {len(max(re.findall(r'[s]+', string)))}")
