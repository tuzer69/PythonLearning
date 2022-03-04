one_class = []
two_class = []
total_class = []

for i_unit in range(160, 177, 2):
    one_class.append(i_unit)
for i_unit in range(162, 181, 3):
    two_class.append(i_unit)

total_class.extend(one_class)
total_class.extend(two_class)

for i_mn in range(len(total_class)):
    for curr in range(i_mn, len(total_class)):
        if total_class[curr] < total_class[i_mn]:
            total_class[curr], total_class[i_mn] = total_class[i_mn], total_class[curr]

print("Итоговый список", total_class)

# зачтено
