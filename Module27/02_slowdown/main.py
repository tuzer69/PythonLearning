import random
import time
from typing import Callable


def sleep_dec(func: Callable) -> Callable:
    """
    Декоратор добавляет задержку для функции
    :param func: Декорируемая функция
    :return: Функция

    """
    def wrapper(*args, **kwargs):
        print('Working........')
        time.sleep(random.randint(2, 5))
        func(*args, **kwargs)
    return wrapper


@sleep_dec
def f1(x: int, y: int):
    x += random.randint(10, 100)
    y += random.randint(10, 100)
    print(round(x / y, 2))


f1(12, 34)
