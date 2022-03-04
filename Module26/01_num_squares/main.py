from collections.abc import Iterator
from collections.abc import Iterable


class squre_ite:
    def __init__(self, N: int) -> None:
        self.__n = N
        self.__curr = 0

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> Iterable[int]:
        if self.__curr < self.__n:
            self.__curr += 1
            return self.__curr ** 2
        else:
            raise StopIteration


def squre_gen(N: int) -> Iterable[int]:
    __current = 1
    for _ in range(N):
        yield __current ** 2
        __current += 1


evalution = (n ** 2 for n in range(1, 11))
