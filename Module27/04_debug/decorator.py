from typing import Callable


def debug(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        argsTmp = []
        for argument in args, kwargs:
            if isinstance(argument, dict) and argument != {}:
                for i_key, i_value in argument.items():
                    argsTmp.append(str(i_key) + '=' + str(i_value))
            elif isinstance(argument, tuple) and argument != ():
                argsTmp.append(argument[0])
        arguments = argsTmp[0]
        if len(argsTmp) > 1:
            for i_arg in range(1, len(argsTmp)):
                arguments += str(', ' + argsTmp[i_arg])
        ret = func(*args, **kwargs)
        result = ("Вызывается: {0}({1})\n'{0}' вернула значение '{2}'".
                  format(func.__name__, arguments, ret))
        print(result)
        return ret
    return wrapper
