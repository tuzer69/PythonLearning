def check_num(num):
    n0 = ""
    n1 = ""
    n2 = ""
    n3 = ""
    count = 1
    for i in str(num):
        if n0 == "":
            n0 = i
        elif n1 == "":
            n1 = i
            if n1 == n0:
                count += 1
        elif n2 == "":
            n2 = i
            if n2 == n0 or n2 == n1:
                count += 1
        else:
            n3 = i
            if (n3 == n0 and n3 == n1) or (n3 == n0 and n3 == n2) or (n3 == n1 and n3 == n2):
                count += 1
    if count == 3:
        return True
    else:
        return False


A = int(input("Введите первый год: "))
B = int(input("Введите второй год: "))
print("Годы от ", A, "до", B, "с тремя одинаковыми цифрами:")
for n in range(A, B + 1):
    if check_num(n):
        print(n)

# зачтено
