envelope = 12
letter = int(input('Размер листа (см): '))
fold = 0

while letter > envelope:
    fold += 2
    letter /= 2

print(f"Что бы письмо поместилось в конверт его нужно {fold} раз(а) сложить пополам")
