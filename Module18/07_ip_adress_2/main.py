def check_ip(address):
	ip_list = address.split('.')
	for i_ip in ip_list:
		if len(ip_list) < 4:
			print("Адрес - это четыре числа, разделённые точками")
			return False
		elif not i_ip.isdigit():
			print(i_ip, "не целое число")
			return False
		elif int(i_ip) > 255:
			print(i_ip, "превышает 255")
			return False
	return True


if check_ip(input("Введите IP: ")):
	print("IP-адрес корректен")






