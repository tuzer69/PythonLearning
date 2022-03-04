cells = [3, 0, 6, 2, 10]
print("Количество клеток: ", len(cells))
bad_cells = []
for i in range(len(cells)):
    print("Эффективность", i + 1, "клетки: ", cells[i])
    if cells[i] < i:
        bad_cells.append(cells[i])
print("Не подходящие значения: ", end='')
for i in bad_cells:
    print(i, " ", end='')

# зачтено
