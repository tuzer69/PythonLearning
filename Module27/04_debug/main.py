from decorator import debug


@debug
def greeting(name: str, age: int = None) -> str:
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".\
            format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


print('=' * 40)
print(greeting("Том"))
print('=' * 40)
print(greeting("Миша", age=100))
print('=' * 40)
print(greeting(name="Катя", age=16))
print('=' * 40)
