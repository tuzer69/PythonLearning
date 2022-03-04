list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

try:
    for x in list_1:
        for y in list_2:
            result = x * y
            print(x, y, result)
            if result in (x * y for x in list_1 for y in list_2
                          if x * y == to_find):
                print('Found!!!')
                raise StopIteration

except StopIteration: pass
