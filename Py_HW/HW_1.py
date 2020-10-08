def division(num_1, num_2):
    try:
        return num_1 / num_2
    except ZeroDivisionError:
        print('division by zero')


print(division(10, 0))
