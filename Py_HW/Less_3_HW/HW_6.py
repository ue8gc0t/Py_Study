def int_func(word):
    return word.capitalize()


def int_func2(string):
    return ' '.join(map(int_func, string.split()))


print(int_func2(input('Write string: ')))
