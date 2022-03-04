N = int(input('Введите кол-во заказов: '))
orders = {}
order = ""

for i_order in range(1, N + 1):
	print(i_order, 'Заказ: ', end='')
	order = input().split()
	if orders.get(order[0], {}):
		if orders[order[0]].get(order[1], {}):
			orders[order[0]][order[1]] += int(order[2])
		else:
			orders[order[0]][order[1]] = int(order[2])
	else:
		orders[order[0]] = {order[1]: int(order[2])}
print()
for i_client in sorted(orders.keys()):
	print(i_client + ':')
	for i_pizza in sorted(orders[i_client].keys()):
		print('\t', i_pizza + ':', orders[i_client].get(i_pizza, {}))

