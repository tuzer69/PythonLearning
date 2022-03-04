from decorators import logging


@logging
def add_binary(a, b):
    """
    Возвращает сумму двух десятичных чисел в двоичном формате.

            Параметры:
                    a (int): первое десятичное целое число
                    b (int): второе десятичное целое число

            Возвращаемое значение:
                    binary_sum (str): двоичная строка суммы a и b
    """
    binary_sum = bin(a+b)[2:]
    return binary_sum


print(add_binary(2, 2, 4))
print(add_binary(2, 4))
