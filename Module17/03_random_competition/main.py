import random
first_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
second_team = [round(random.uniform(5, 10), 2) for _ in range(20)]

print("Первая команда: ", first_team)
print("Вторая команда: ", second_team)
print()
print("Победители тура: ", [first_team[i_item] if first_team[i_item] > second_team[i_item]
							else second_team[i_item]
							for i_item in range(len(first_team))])
