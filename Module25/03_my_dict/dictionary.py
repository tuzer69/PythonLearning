class MyDict:
    __words = {}

    def __getitem__(self, item):
        return self.__words[item]

    def __setitem__(self, key, value):
        self.__words[key] = value

    def get(self, key):
        if self.__words.get(key):
            return self.__words[key]
        else:
            return 0

    def clear(self):
        self.__words = {}

    def items(self):
        return self.__words

    def keys(self):
        return self.__words.keys()

    def pop(self, key):
        return self.__words.pop(key)

    def popitem(self):
        return self.__words.popitem()

    def values(self):
        return self.__words.values()