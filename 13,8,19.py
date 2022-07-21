all_tickets = int(input("Количество покупаемых билетов: "))
ages = []
for i in range(all_tickets):
    age_ = int(input("Возраст отдельного посетителя: "))
    ages.append(age_)
full_cost = 0
for i, value in enumerate(ages):
    if 18 <= value <= 25:
        full_cost += 990
    elif 25 < value:
        full_cost += 1390
    elif all_tickets > 3:
        full_cost -= full_cost * 0.1
print("Полная стоимость покупки: ", full_cost)
