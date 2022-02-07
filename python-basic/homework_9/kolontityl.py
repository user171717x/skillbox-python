total_len = int(input('Общая длина колонтитула в символах: '))
wow_count = int(input('Желаемое количество восклицательных знаков: '))
before = (total_len - wow_count) // 2
after = total_len - before - wow_count
print(f"{'~' * before}{'!' * wow_count}{'~' * after}")
