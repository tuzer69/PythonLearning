orig = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Первый способ:
new_list = []
for i_ in range(0, len(orig), 2):
	new_list.append((orig[i_], orig[i_ + 1]))
print(new_list)


# Второй способ:
new_list = [(orig[x], orig[x + 1]) for x in range(len(orig)) if x % 2 == 0]
print(new_list)
