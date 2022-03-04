from typing import Callable, Optional
from functools import wraps


def singleton(func: Callable) -> Callable:
    instances = {}

    def getinstance(*args, **kwargs) -> Callable:
        if func not in instances:
            instances[func] = func(*args, **kwargs)
        return instances[func]

    return getinstance


@singleton
def sum(x, y) -> int:
    print(x + y)


sum(4, 3)
sum(4, 8)
sum(4, 5)
sum(4, 8)
