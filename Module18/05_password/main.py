def check_capital(string):
	for i_sym in string:
		if i_sym.isupper():
			return True
	return False


def check_digit(string):
	count = 0
	for i_sym in string:
		if i_sym.isdigit():
			count += 1
	if count >= 3:
		return True
	else:
		return False


while True:
	password = input("Придумайте пароль: ")
	if not check_capital(password) or len(password) < 8 or not check_digit(password):
		print("Пароль ненадёжный. Попробуйте ещё раз.")
	else:
		print("Это надёжный пароль!")
		break
