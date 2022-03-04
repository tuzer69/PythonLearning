import os
from typing import Generator


def gen_files_path(cat: str, path: str = "C:\\") -> Generator:
    p = os.path.join(path, cat)
    if not os.path.exists(p):
        print('Указанный каталог не судестует!')
        return None
    return (os.path.join(p, f) for f in os.listdir(p)
            if os.path.isfile(os.path.join(p, f)))


gen = gen_files_path("System32", "C:\\Windows\\")
for i_file in gen:
    print(i_file)
