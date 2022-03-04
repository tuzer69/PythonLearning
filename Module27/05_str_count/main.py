from typing import Callable
from random import randint


def counter(func: Callable) -> Callable:
    counters = {}

    def wrapper(*args, **kwargs):
        counters[func] = counters.get(func, 0) + 1
        print(f'Функция {func.__name__} вызвана {counters[func]} раз')
        return func(*args, **kwargs)
    return wrapper


@counter
def some_function(x: int, y: int):
    x += randint(10, 100)
    y += randint(10, 100)
    return round(x / y, 2)


print(some_function(3, 5))
print(some_function(3, 5))
print(some_function(3, 5))
print(some_function(3, 5))
print(some_function(3, 5))
