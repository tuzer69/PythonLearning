math_operators = ['//', '/', '*', '+', '-', '%']


def math_operation(val1, val2, operation):
    try:
        if operation not in math_operators:
            raise TypeError
        elif not str(val1).isdigit() or not str(val2).isdigit():
            raise TypeError
        elif operation == '//': return int(val1) // int(val2)
        elif operation == '/' : return int(val1) / int(val2)
        elif operation == '*' : return int(val1) * int(val2)
        elif operation == '+' : return int(val1) + int(val2)
        elif operation == '-' : return int(val1) - int(val2)
        elif operation == '%' : return int(val1) % int(val2)
    except ZeroDivisionError:
        print('Деление на ноль недопустимо')


summa = 0
with open('calc.txt', 'r', encoding='utf-8') as calc_file:
    for i_line in calc_file:
        try:
            expression = i_line.split()
            summa += math_operation(expression[0],
                                    expression[2], expression[1])
        except TypeError:
            print('Неверно указан тип операнда')
        except IndexError:
            print('НЕ верный формат выражения')

    print('Сумма всех верных строк равна: ', summa)
