from typing import Callable
from utils import write_log
import datetime


def logging(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print('Функция: {0}'.format(func.__name__))
        print(func.__doc__)
        try:
            result = func(*args, **kwargs)
        except Exception as ex:
            dt = datetime.datetime.now()
            error = f'Ошибка: {ex}' \
                    f'\nФункция: {func.__name__} ' \
                    f'\nДата: {dt.strftime("%m.%d.%Y")}' \
                    f'\nВремя: {dt.strftime("%H:%M:%S")}'
            write_log(error)
    return wrapper
