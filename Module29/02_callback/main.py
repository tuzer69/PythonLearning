from typing import Callable, Optional
from time import time, sleep
import functools


def callback(i_func, path: str = '//') -> Callable:
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            if 'index' in path:
                sleep(1)
                i_func()
        return wrapper

    return decorator


def callback_func() -> None:
    print('Пример функции, которая возвращает ответ сервера')


@callback(i_func=callback_func, path='https://index.html')
def example() -> None:
    print('Loading........')


example()
