import random
N = int(input("Введите длину списка: "))
lst = [(random.randint(1, 20) // 5 if i % 2 != 0 else 1) for i in range(1, N + 1)]
print("Результат:", lst)