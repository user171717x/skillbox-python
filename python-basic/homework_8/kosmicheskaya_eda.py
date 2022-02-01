food_total = 100
food_per_month = 4
month = 0

for eated in range(food_per_month, food_total + food_per_month, food_per_month):
    month += 1
    print(f"{food_total - eated} kg food left after {month} month")
