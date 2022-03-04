N = input("Введите строку: ")
new_str = []
prv_sym = ""
count = 1
for i_sym in range(len(N)):
	if N[i_sym] == prv_sym:
		count += 1
		prv_sym = N[i_sym]
		if i_sym == len(N) - 1:
			new_str.append(N[i_sym] + str(count))
	else:
		if prv_sym != "":
			new_str.append(prv_sym + str(count))
		prv_sym = N[i_sym]
		count = 1
		if i_sym == len(N) - 1:
			new_str.append(N[i_sym] + str(count))

print("Закодированная строка:", ''.join(new_str))
