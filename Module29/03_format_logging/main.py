import time
from typing import Callable, Optional
from datetime import datetime
from functools import wraps


def convertDate(data: str):
    newData = ''
    for i_sym in data:
        if i_sym.isalpha():
            newData += '%' + i_sym
        else:
            newData += i_sym
    return newData


def timer(func, time_format):
    @wraps(func)
    def wrapper(*args, **kwargs):
        date_format = convertDate(time_format)
        print(f'Запускается {wrapper.__qualname__} Дата и время запуска: '
              f'{datetime.strftime(datetime.today(), date_format)}')
        start = time.time()
        result = func(*args, **kwargs)
        print(f'Завершение {wrapper.__qualname__}, время работы: '
              f'{round(time.time() - start, 3)}s')
        return result

    return wrapper


def log_methods(_dec: Optional[Callable] = None, fomt: str = '') -> Callable:
    @wraps(_dec)
    def wrapper(cls):
        for i_method_name in dir(cls):
            if i_method_name.startswith('__') is False:
                curr_method = getattr(cls, i_method_name)
                decorated_method = timer(curr_method, fomt)
                setattr(cls, i_method_name, decorated_method)
        return cls

    return wrapper


@log_methods(fomt='b d Y - H:M:S')
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = A()
my_obj.test_sum_1()
my_obj.test_sum_2()
