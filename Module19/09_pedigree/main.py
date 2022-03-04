N = int(input('Введите количество человек: '))
gen_tree = {}
for i_pair in range(1, N):
	print(i_pair, 'пара:', end=' ')
	pair = input().split()
	if not gen_tree.get(pair[1], {}):
		gen_tree[pair[1]] = 0
		gen_tree[pair[0]] = gen_tree[pair[1]] + 1
	else:
		gen_tree[pair[0]] = gen_tree[pair[1]] + 1

print('“Высота” каждого члена семьи:')
for i_key in sorted(gen_tree.keys()):
	print(i_key, gen_tree.get(i_key))
