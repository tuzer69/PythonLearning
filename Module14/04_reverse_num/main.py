def revers_num(num):
    f = ""
    s = ""
    rev = False
    for i in str(num):
        if i == '.':
            rev = True
            continue
        if not rev:
            f = i + f
        elif rev:
            s = i + s
    return float(str(f + '.' + s))


N = float(input("Введите первое число: "))
K = float(input("Введите второе число: "))
print()
print("Первое число наоборот: ", revers_num(N))
print("Второе число наоборот: ", revers_num(K))
print("Сумма: ", revers_num(N) + revers_num(K))

# зачтено
