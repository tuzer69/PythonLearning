def summa(num):
    n_sum = 0
    while num > 0:
        n_sum += num % 10
        num //= 10
    return n_sum


def diff(num):
    count = 0
    for i in str(num):
        count += 1
    return count


number = int(input("Введите число: "))
print("Сумма цифр: ", summa(number))
print("Кол-во цифр в числе: ", diff(number))
print("Разность суммы и кол-ва цифр: ", summa(number) - diff(number))

# зачтено
