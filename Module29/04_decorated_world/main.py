from typing import Callable, Optional, Any
from functools import wraps


def decorator_with_args_for_any_decorator(decorator_to_enhance: Callable) -> Callable:
    """ Декоратор. Даёт возможность другому декоратору принимать произвольные аргументы """
    def decorator_maker(*args, **kwargs) -> Callable:
        def decorator_wrapper(func: Callable) -> Callable:
            return decorator_to_enhance(func, *args, **kwargs)
        return decorator_wrapper
    return decorator_maker


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs) -> Callable:
    """ Декоратор. Шаблон """
    @wraps(func)
    def wrapper(function_arg1: Optional[Any], one_args: Optional[Any]) -> \
            Callable:
        print("Переданные арги и кварги:", args, kwargs)
        return func(function_arg1, one_args)
    return wrapper


@decorated_decorator(10000, 69999)
def decorated_function(text: str, num: int) -> None:
    """ Пример декорируемой функции """
    print("Привет", text, num)


decorated_function("User", 1001)
