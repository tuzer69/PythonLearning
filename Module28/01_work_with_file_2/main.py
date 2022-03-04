class File:
    def __init__(self, name: str, mode: str = 'r') -> None:
        self.__name = name
        self.__mode = mode
        self.__file = None

    def __enter__(self) -> None:
        try:
            self.__file = open(self.__name, self.__mode, encoding='utf-8')
        except FileNotFoundError:
            self.__file = open(self.__name, 'w', encoding='utf-8')
        return self.__file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        return True


with File('text.txt', 'a') as reader:
    reader.write("EXAMPLE....")
