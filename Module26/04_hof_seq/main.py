from collections.abc import Iterator
from collections.abc import Iterable


class QHofstadter:
    def __init__(self, s: list) -> None:
        self.s = s[:]

    def __next__(self) -> Iterable[int]:
        try:
            q = self.s[-self.s[-1]] + self.s[-self.s[-2]]
            self.s.append(q)
            return q
        except IndexError:
            raise StopIteration()

    def __iter__(self) -> Iterator:
        return self

    def current_state(self) -> list:
        return self.s


qq = QHofstadter([1, 1])
print([next(qq) for __ in range(20)])
