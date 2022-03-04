from typing import Callable, Optional
import functools


def check_permission(_func: Optional[Callable] =
                     None, *, user: str = 'noname') -> Callable:
    def check_decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if user.lower() == 'admin':
                func()
            else:
                raise PermissionError('У пользователя недостаточно прав')
            return
        return wrapper
    if _func is None:
        return check_decorator
    return check_decorator(_func)


@check_permission(user='admin')
def delete_site() -> None:
    print('Удаляем сайт')


@check_permission(user='user_1')
def add_comment() -> None:
    print('Добавляем комментарий')


try:
    delete_site()
    add_comment()
except PermissionError:
    print('PermissionError: У пользователя недостаточно прав,'
          ' чтобы выполнить функцию add_comment')
