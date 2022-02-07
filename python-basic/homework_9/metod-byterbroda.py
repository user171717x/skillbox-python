message = input('Введите зашифрованное сообщение: ')    # 'shacnidw' 'Sounp-etre-rSce'
print('Расшифрованное сообщение: ', end='')
for idx in range(0, len(message), 2):
    print(message[idx], end='')
for idx in range(len(message) - (2 if len(message) % 2 else 1), 0, -2):
    print(message[idx], end='')
print('')