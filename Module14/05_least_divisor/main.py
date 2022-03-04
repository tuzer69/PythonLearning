def min_dev(num):
    for i in range(2, num + 1):
        if num % i == 0:
            return i


N = int(input("Введите число: "))
print("Наименьший делитель, отличный от единицы: ", min_dev(N))

# зачтено
