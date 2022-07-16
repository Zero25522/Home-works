per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
per_cent1 = per_cent.values()

money = int(input('Сумма вклада:'))
deposit = []
for i, value in enumerate(per_cent1):
    sp = money * value / 100
    deposit.append(sp)
print(deposit)

print('Максимальная сумма, которую вы можете заработать -', max(deposit))