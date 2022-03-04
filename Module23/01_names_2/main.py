counts = 0

with open('people.txt', 'r', encoding='utf-8') as people_file:
	cur_str = 1
	for i_line in people_file:
		line_count = 0
		try:
			for i_sym in i_line:
				if i_sym.isalpha():
					line_count += 1
			if line_count < 3:
				raise BaseException()
			cur_str += 1
			counts += line_count
		except BaseException:
			print('В строке #', cur_str, ' меньше 3 символов', sep='')
			with open('errors.log', 'a', encoding='utf-8') as errors_log:
				errors_log.write('Error: ' + 'В строке #' +
								 str(cur_str) + ' меньше 3 символов' + '\n')

print('Общее количество символов:', counts)
