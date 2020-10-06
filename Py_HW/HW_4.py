# def my_func(x, y):
#     return x ** y

def my_func(x, y):
    i = 0
    result = 1
    while i < abs(y):
        result = result / x
        i += 1
    return result


print(my_func(4, -2))

