N = int(input('Кол-во стран: '))
country = []
country_dict = {}

for i_ in range(1, N + 1):
	print(i_, 'страна:', end=' ')
	country = input().split()
	country_dict.update({s:country[0] for s in country[1:]})

for i_ in range(1, 4):
	print(i_, 'город:', end=' ')
	town = input()
	if country_dict.get(town, {}):
		print('Город', town, 'расположен в стране', country_dict.get(town, {}))
	else:
		print('По городу', town, 'нет данных')
