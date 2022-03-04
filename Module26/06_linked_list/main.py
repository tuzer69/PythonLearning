from collections.abc import Iterator
from collections.abc import Iterable


class Data:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.current = None

    def __iter__(self) -> Iterator:
        self.current = self.head
        return self

    def __next__(self) -> Iterable:
        if self.current:
            value = self.current.value
            self.current = self.current.next
            return value
        else:
            raise StopIteration

    def append(self, value: int) -> None:
        newValue = Data(value)
        if self.head is None:
            self.head = newValue
            return
        lastElem = self.head
        while lastElem.next:
            lastElem = lastElem.next
        lastElem.next = newValue

    def get(self, index: int) -> int:
        item = self.head
        curr_index = 0
        try:
            while curr_index <= index:
                if curr_index == index:
                    return item.value
                curr_index += 1
                item = item.next
        except AttributeError: pass

    def remove(self, index: int) -> None:
        item = self.head
        curr_index = 0
        try:
            while curr_index < index:
                if curr_index == index - 1 and item.next:
                    item.next = item.next.next
                    return
                curr_index += 1
                item = item.next
        except AttributeError: pass


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.append(50)
for i in my_list:
    print(i)

print('=' * 10)

my_list.remove(6)
for i in my_list:
    print(i)
