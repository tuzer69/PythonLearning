import os

second_tour = []

with open('first_tour.txt', 'r', encoding='utf-8') as f_tour:
	score = int(f_tour.readline())
	for i_line in f_tour:
		tmp = i_line.split()
		if int(tmp[2]) > score:
			second_tour.append(tmp)

with open('second_tour.txt', 'w', encoding='utf-8') as s_tour:
	s_tour.write(str(len(second_tour)) + '\n')
	num_str = 1
	while len(second_tour) > 0:
		del_index = 0
		select_elem = second_tour[0]
		for i_elem in range(len(second_tour)):
			if int(second_tour[i_elem][2]) > int(select_elem[2])\
					or len(second_tour) == 1:
				select_elem = second_tour[i_elem]
				del_index = i_elem
		second_tour.pop(del_index)
		w_str = '{0}) {1} {2} {3}'.format(
			num_str,
			select_elem[0][0] + '.',
			select_elem[1],
			select_elem[2])
		s_tour.write(w_str + '\n')
		num_str += 1
