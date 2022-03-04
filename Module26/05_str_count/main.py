from collections.abc import Iterable
import os


def get_files(path: str) -> Iterable[str]:
    __list = []
    for i_file in os.listdir(path):
        if str(i_file).endswith('.py'):
            __list.append(i_file)
    return __list


def str_count(path: str) -> int:
    files = get_files(path)
    for i_file in files:
        with open(i_file, 'r', encoding='utf-8') as file:
            for i_line in file:
                if i_line != '\n' and not i_line.startswith('#'):
                    yield i_line


gen = str_count(os.path.abspath('.'))
count = 0
for _ in gen:
    count += 1
print('Всего строчек кода:', count)
