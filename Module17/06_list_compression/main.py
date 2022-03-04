import random

N = [random.randint(0, 4) for _ in range(10)]
print("Список до сжатия: ", N)
sort_list = [N[i_item] for i_item in range(len(N)) if N[i_item] > 0] + [0 for _ in range(N.count(0))]
print("Отсортированный список", sort_list)
print("Спикок после сжатия", sort_list[:sort_list.index(0)])
