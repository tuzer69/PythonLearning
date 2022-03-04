def shortest(*args):
    return range(len(sorted(args, key=len)[0]))


def my_zip(first, second):
    result = ((first[i], second[i]) for i in shortest(first, second))
    return result
