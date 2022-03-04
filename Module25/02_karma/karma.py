import random
import exeptions


class Karma:
    __karma = 0
    __exeptions = []

    def __init__(self):
        self.__exeptions.append(exeptions.KillError())
        self.__exeptions.append(exeptions.DrunkError())
        self.__exeptions.append(exeptions.CarCrashError())
        self.__exeptions.append(exeptions.GluttonyError())
        self.__exeptions.append(exeptions.DepressionError())

    def get_karma(self):
        return self.__karma

    def one_day(self):
        self.__karma += random.randint(1, 7)
        r = random.randint(1, 10)
        if r == 5:
            r = random.randint(1, len(self.__exeptions) - 1)
            raise self.__exeptions[r]


