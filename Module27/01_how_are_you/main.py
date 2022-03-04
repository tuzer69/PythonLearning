import random
from typing import Callable


def how_are_you(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию')
        func(*args, **kwargs)
    return wrapper


@how_are_you
def f1(x: int, y: int):
    x += random.randint(10, 100)
    y += random.randint(10, 100)
    print(round(x / y, 2))


@how_are_you
def f2(x: int, y: int):
    x -= random.randint(10, 100)
    y -= random.randint(10, 100)
    print(round(y / x, 2))


f1(3, 5)
f2(4, 8)
