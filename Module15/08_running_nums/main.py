N = [1, 2, 3, 4, 5]
shift_N = []
K = int(input("Введите сдвиг (от 1 до 5): "))
while (K < 0) or (K > 5):
    K = int(input("Введите сдвиг (от 1 до 5): "))
for i in range(-K, len(N) - K, 1):
    shift_N.append(N[i])

print("Изначальный список: ", N)
print("Сдвинутый список: ", shift_N)

# зачтено
